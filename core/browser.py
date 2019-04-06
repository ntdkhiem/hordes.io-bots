import pickle
import logging
from os.path import isfile
from selenium import webdriver
from selenium.common import exceptions

URL = 'https://hordes.io'


class Driver:

    def __init__(self, type: str,
                 # total: int        # total web browser to open
                 ):
        self.logger = logging.getLogger('hordes.io')
        # self.browser = self.set_web_driver(type)
        if not type:
            self.logger.warning('No web browser specify')
            return
        self.logger.info(f"Setting options for {type}...")
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
            self.logger.error(f"{type} is not supported")
            return

        # Load cookies if exist
        if isfile("hordes_cookies.pkl"):
            self.logger.info("Adding cookies to browser...")
            for cookie in pickle.load(open("hordes_cookies.pkl", "rb")):
                self.driver.add_cookie(cookie)

    def start(self):
        # Launch web browser
        self.logger.info("Starting web browser")
        # TODO: add firefox's capability
        # NOTE: for chrome only
        try:
            self.driver = self.driver(chrome_options=self.chrome_options)
        except exceptions.WebDriverException:
            self.logger.exception('Could not initiate web driver')
            return

        self.driver.get(URL)
        return self.driver

    def quit(self):
        """
        Save cookies from session and destroy driver
        """
        # Save cookies to hordes_cookies.pkl
        self.logger.info("Saving cookies...")
        pickle.dump(self.driver.get_cookies(), open("hordes_cookies.pkl", "wb"))
        # quitting
        self.logger.info("Quitting driver...")
        self.driver.quit()




