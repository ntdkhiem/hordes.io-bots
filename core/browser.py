import pickle
from sys import exit
from core.setup_logger import logger
from os.path import isfile
from selenium import webdriver
from selenium.common import exceptions

URL = 'https://hordes.io'


class Driver:

    def __init__(self, type: str,
                 # total: int        # total web browser to open
                 ):
        # self.browser = self.set_web_driver(type)
        if not type:
            logger.warning('No web browser specify')
            return
        logger.info(f"Setting options for {type}...")
        if type.lower() == "chrome":
            from selenium.webdriver.chrome.options import Options
            self.driver = webdriver.Chrome
            # Initialize options:
            self.chrome_options = Options()
            # Load Web Page with Disk Cache
            preferences = {'disk-cache-size': 4096}
            self.chrome_options.add_experimental_option('prefs', preferences)
            # Additional options
            self.chrome_options.add_argument('--disable-extensions')
            self.chrome_options.add_argument("--disable-gpu")
            self.chrome_options.add_argument('--start-maximized')
        elif type.lower() == "firefox":
            self.driver = webdriver.Firefox
            # TODO: add options for firefox
        else:
            logger.error(f"{type} is not supported")
            return

        # Load cookies if exist
        if isfile("hordes_cookies.pkl"):
            logger.info("Adding cookies to browser...")
            for cookie in pickle.load(open("hordes_cookies.pkl", "rb")):
                self.driver.add_cookie(cookie)

    def start(self):
        # Launch web browser
        logger.info("Starting web browser...")
        # TODO: add firefox's capability
        # NOTE: for chrome only
        try:
            self.driver = self.driver(chrome_options=self.chrome_options)
        except exceptions.WebDriverException:
            logger.error('Could not initiate web driver...')
            exit(1)
        except KeyboardInterrupt:
            logger.warning('Quited...')
            exit(1)

        self.driver.get(URL)
        return self.driver

    def quit(self):
        """
        Save cookies from session and destroy driver
        """
        # Save cookies to hordes_cookies.pkl
        logger.info("Saving cookies...")
        pickle.dump(self.driver.get_cookies(), open("hordes_cookies.pkl", "wb"))
        # quitting
        logger.info("Quitting driver...")
        self.driver.quit()




