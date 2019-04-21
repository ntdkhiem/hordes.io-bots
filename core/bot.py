import time
from abc import ABC, abstractmethod
from core.setup_logger import logger
from selenium.webdriver.common.keys import Keys

URL = 'https://hordes.io'
DELAY = 0.1             # bot's lifespan
LOW_MANA_LIMIT = 30
RANDOM_MOVE_COUNT = 5       # After x loops then randomly move to avoid bot-like behaviour


class Bot(ABC):  # Root class
    def __init__(self, driver_obj):
        self.webdriver = driver_obj
        self.driver = self.webdriver.driver
        self.driver.execute_script("alert('Please press Enter in the terminal when logged in and on the play screen');")
        input("[+] Press ENTER when you're login in and on the play screen (make sure to place me at the grinding spot)... ")
        # Get necessary components
        logger.info('Getting components...')
        self.components = self.get_components()
        self.action = self.driver.find_element_by_tag_name('body')

    def run(self):
        """
        Main loop for the bot
        """
        logger.info('Bot is running...')
        enemy_is_alive = False
        enemy_previous_health = -1                 # to check if the enemy actually get damaged
        random_move_countdown = RANDOM_MOVE_COUNT
         
        while True:
            try:
                if self.components:
                    print(self.components)
                    self.player = self.components.get('player')
                    self.enemy = self.components.get('target')
                    logger.debug("Checking player's health...")
                    player_health_status = self.check_health()
                    logger.debug("Checking player' mana...")
                    player_mana_status = self.check_mana()

                    if enemy_is_alive and self.enemy.get('is_alive'):
                        # check for player's health status
                        if player_health_status is 'low':
                            # if 'low' then heal up
                            logger.info("Player's health is low. Defending...")
                            self.defend()
                            # if 'die' then respawn
                        elif player_health_status is 'die':
                            logger.info("Player's died. Respawning...")
                            self.driver.execute_script("alert('Player died...');")
                            self.respawn()    
                            input("Please lead me to the griding location and press ENTER...")
                            continue
                            # if 'normal' then continue 
                        else:
                            logger.debug("Player's health is normal...")
                        
                        # check for player's mana status
                        if player_mana_status is 'low':
                            # if 'low' then rest
                            logger.info(f"Player's mana is low. Resting...")
                            self.rest()
                            # if 'normal' then continue
                        else:
                            logger.debug("Player's mana is normal...")

                        # check for enemy's health status
                        logger.debug("Checking enemy's health...")
                        enemy_health_status = self.check_enemy_health()
                        if enemy_health_status is 'die':
                            # if 'die' then find another enemy
                            logger.debug("Enemy died...")
                            enemy_is_alive = False
                            enemy_previous_health = -1
                            continue
                            # if 'alive' then continue
                        else:
                            logger.debug("Enemy is still alive...")
                            if enemy_previous_health == enemy_health_status:                # Checking if the attack could damage the target
                                logger.info("Player could not damage the enemy. Find another one...")
                                enemy_is_alive = False
                                enemy_previous_health = -1
                                continue
                            enemy_previous_health = enemy_health_status
                        # Attack reached the target 

                        # attack the enemy
                        logger.debug("Attacking the target...")
                        self.attack()   

                        # Randomly move
                        if random_move_countdown == 0:
                            logger.debug('Performing random move...')
                            self.random_move()
                            random_move_countdown = RANDOM_MOVE_COUNT
                        else:
                            random_move_countdown -= 1
                    else:
                        # update enemy's status
                        logger.debug("Finding another enemy...")
                        self.find_enemy()
                        enemy_is_alive = True

                    # Everything goes smoothly
                    time.sleep(DELAY)
                    # update status
                    self.components = self.get_components()
                else:
                    logger.warning('Lost control of the bot...')
                    raise Exception('Could not find neccessary components for bot...')          # TODO: change to specific exception to raise.
                
            except Exception as e:
                logger.exception(e)
                logger.warning('Bot is disconnecting...')
                self.quit()

    @abstractmethod
    def attack(self): 
        """
        Inheritable attacking method for subclass (all characters have different move)
        """
        pass
    
    @abstractmethod
    def defend(self):
        """
        Inheritable heal method for subclass (all characters have different move)
        """
        pass
    
    def random_move(self):
        """
        Random move to avoid potential-like bot
        """
        # TODO: implement this method
        pass

    def rest(self):
        """
        Resting for 2 seconds
        """
        # TODO: Improve on this method
        rest_time = 2
        time.sleep(rest_time)
    
    def find_enemy(self):
        """
        Send "TAB" as a shortcut to find enemy 
        """
        self.action.send_keys(Keys.TAB)
    
    def check_health(self):
        """
        Check player's health. If player's health is less than half of max_health then return 'low' or 'die' if died else 'normal'  
        """
        current_health = int(self.player.get('current_health'))
        max_health = int(self.player.get('max_health'))
        if current_health == 0:
            return 'die'
        
        return 'low' if current_health < max_health // 2 else 'normal' 
    
    def check_mana(self):
        """
        Check player's mana. If player's mana is less than or equal MANA_LIMIT then return 'low' else 'normal'
        """
        current_mana = int(self.player.get('current_mana'))
        
        return 'low' if current_mana <= LOW_MANA_LIMIT else 'normal'
    
    def check_enemy_health(self):
        """
        Check enemy's health. If enemy died return 'die' else return its current health
        """
        current_health = self.enemy.get('current_health')
        if current_health:
            current_health = int(current_health)
        else:
            current_health = 0

        return 'die' if current_health == 0 else current_health

    def respawn(self):
        """
        Click respawn button 
        """
        respawn_btn = self.driver.find_element_by_xpath('//*[@id="ui_btn_respawn"]')
        respawn_btn.click()

    def get_components(self):
        """
        Find and get all components (health bar, mana bar, info)
        :return: Dictionary of components
        """
        components = dict()
        try:
            components = {
                'player': {
                    'current_health': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                        'div[1]/div[2]/span[1]').text,
                    'max_health': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                    'div[1]/div[2]/span[2]').text,
                    'current_mana': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                      'div[2]/div[2]/span[1]').text,
                },
                'target': {
                    'is_alive': self.driver.find_element_by_xpath('//*[@id="ui_target"]').is_displayed(),
                    'current_health': self.driver.find_element_by_xpath('//*[@id="ui_target"]/div/'
                                                                        'div[1]/div[2]/span[1]').text,
                }
            }
        except AttributeError:
            logger.error('Could not retrieve necessary components...')
        finally:
            return components

    def quit(self):
        self.webdriver.quit()
