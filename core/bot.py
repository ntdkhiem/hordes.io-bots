from abc import ABC, abstractmethod
from core.setup_logger import logger

URL = 'https://hordes.io'


class Bot(ABC):  # Root class
    def __init__(self, driver):
        self.driver = driver
        input("[+] Press ENTER when you're login in and on the play screen...")
        # Get necessary components
        self.components = self.get_components()

    @abstractmethod
    def run(self):
        """
        Main loop for the bot
        """
        if self.components:
            logger.info('Bot is running...')
            print('RUNNING')
        else:
            logger.warning('Could not start the bot...')
        return

    def get_components(self):
        """
        Find and get all components (health bar, mana bar, info)
        :return: Dictionary of components
        """
        logger.info('Getting components...')
        try:
            components = {
                'player': {
                    'current_health': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                        'div[1]/div[2]/span[1]').text,
                    'max_health': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                    'div[1]/div[2]/span[2]').text,
                    'current_mana': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                      'div[2]/div[2]/span[1]').text,
                    'max_mana': self.driver.find_element_by_xpath('//*[@id="ui_player"]/div/'
                                                                  'div[2]/div[2]/span[2]').text
                },
                'target': {
                    'is_alive': self.driver.find_element_by_xpath('//*[@id="ui_target"]').is_displayed()
                }
            }
        except AttributeError:
            logger.error('Could not retrieve necessary components...')
            return
        return components

    def quit(self):
        self.driver.quit()
