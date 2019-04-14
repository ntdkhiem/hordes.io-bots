import time
from abc import ABC, abstractmethod
from core.setup_logger import logger
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

URL = 'https://hordes.io'
DELAY = 0.1             # bot's lifespan
LOW_MANA_LIMIT = 30
RANDOM_MOVE_COUNT = 5       # After x loops then randomly move to avoid bot-like behaviour


class Bot(ABC):  # Root class
    def __init__(self, driver_obj):
        self.webdriver = driver_obj
        self.driver = self.webdriver.driver
        input("[+] Press ENTER when you're login in and on the play screen... ")
        # Get necessary components
        logger.info('Getting components...')
        self.components = self.get_components()

    def run(self):
        """
        Main loop for the bot
        """
        logger.info('Bot is running...')
        enemy_is_alive = False
        random_move_countdown = RANDOM_MOVE_COUNT
        while True:
            try:
                if self.components:
                    print(self.components)
                    logger.debug("Checking player's health...")
                    player_health_status = self.check_health()
                    logger.debug("Checking player' mana...")
                    player_mana_status = self.check_mana()
                    enemy = self.components.get('target')

                    logger.debug("Checking for reachable target...")
                    if not self.enemy_is_attackable():
                        logger.debug("Unable to reach the target. Retrying...")
                        enemy_is_alive = False
                    else:
                        logger.debug("Target is reachable...")

                    if enemy_is_alive and enemy.get('is_alive'):
                        # check for player's health status
                        if player_health_status is 'low':
                            # if 'low' then heal up
                            logger.debug("Player's health is low. Healing up...")
                            self.heal()
                            # if 'die' then respawn
                        elif player_health_status is 'die':
                            logger.debug("Player's respawning...")
                            self.respawn()    
                            continue
                            # if 'normal' then continue 
                        else:
                            logger.debug("Player's health is normal...")
                        
                        # check for player's mana status
                        if player_mana_status is 'low':
                            # if 'low' then rest
                            logger.debug(f"Player's mana is low. Resting...")
                            self.rest()
                            # if 'normal' then continue
                        else:
                            logger.debug("Player's mana is normal...")

                        # check for enemy's health status
                        logger.debug("Checking enemy's health...")
                        enemy_health_status = self.check_enemy_health()
                        if enemy_health_status is 'die':
                            # if 'die' then toggle enemy_is_alive to false
                            enemy_is_alive = False
                            continue
                            # if 'alive' then continue
                        else:
                            logger.debug("Enemy is still alive...")

                        # attack the enemy
                        logger.debug("Attacking the target...")
                        self.attack()                                   # TODO: delay to x seconds for cooldown

                        # Randomly move
                        if random_move_countdown == 0:
                            logger.debug('Performing random move...')
                            self.random_move()
                        else:
                            random_move_countdown -= 1
                    else:
                        # update enemy's status
                        logger.debug("Finding another enemy...")
                        self.find_enemy()
                        enemy_is_alive = True

                    # update status
                    self.components = self.get_components()
                else:
                    logger.warning('Lost control of the bot...')
                    raise Exception('Could not find neccessary components for bot...')          # TODO: change to specific exception to raise.
                time.sleep(DELAY)
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
    def heal(self):
        """
        Inheritable heal method for subclass (all characters have different move)
        """
        pass
    
    def random_move(self):
        """
        Random move to avoid potential-like bot
        """
        pass

    def rest(self):
        """
        Resting for 2 seconds
        """
        rest_time = 2
        time.sleep(rest_time)
    
    def find_enemy(self):
        """
        Send "TAB" as a shortcut to find enemy 
        """
        actions = ActionChains(self.driver)
        actions = actions.send_keys(Keys.TAB)
        actions.perform()

    def enemy_is_attackable(self):
        """
        Confirm if the enemy is close to us that attack moves are reachable.
        """
        # attack_overlay = self.attack_main_move.value_of_css_property('position')        # if there is an overlay on one of the attack move then we know that its unable to reach the target

        # return True if attack_overlay == 'static' else False
        return True
    
    def check_health(self):
        """
        Check player's health. If player's health is less than half of max_health then return 'low' or 'die' if died else 'normal'  
        """
        player = self.components.get('player')
        current_health = int(player.get('current_health'))
        max_health = int(player.get('max_health'))
        if current_health == 0:
            return 'die'
        
        return 'low' if current_health < max_health // 2 else 'normal' 
    
    def check_mana(self):
        """
        Check player's mana. If player's mana is less than or equal MANA_LIMIT then return 'low' else 'normal'
        """
        player = self.components.get('player')
        current_mana = int(player.get('current_mana'))
        
        return 'low' if current_mana <= LOW_MANA_LIMIT else 'normal'
    
    def check_enemy_health(self):
        """
        Check enemy's health. If enemy died return 'die' else 'alive'
        """
        enemy = self.components.get('target')
        current_health = int(enemy.get('current_health'))

        return 'die' if current_health == 0 else 'alive'

    def respawn(self):
        """
        Click respawn button 
        """
        respawn_btn = self.driver.find_element_by_xpath('//*[@id="ui_btn_respawn"]')
        respawn_btn.click()

    def get_skills_components(self):
        components = dict()
        try:
            components = {
                'skill_1': self.driver.find_element_by_xpath('//*[@id="ui_skills"]/div[6]'),
                'skill_2': self.driver.find_element_by_xpath('//*[@id="ui_skills"]/div[7]'),
                'skill_3': self.driver.find_element_by_xpath('//*[@id="ui_skills"]/div[8]'),
                'skill_4': self.driver.find_element_by_xpath('//*[@id="ui_skills"]/div[9]'),
            }
        except AttributeError:
            logger.error('Could not retrieve skills elements...')
        finally:
            return components

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
                                                                        'div[1]/div[2]/span[1]').text
                }
            }
        except AttributeError:
            logger.error('Could not retrieve necessary components...')
        finally:
            return components

    def quit(self):
        self.webdriver.quit()
