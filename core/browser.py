import pickle
from core.setup_logger import logger
from os.path import isfile
from selenium import webdriver
from selenium.common import exceptions

URL = 'https://hordes.io'

class Driver:

    def __init__(self, type: str,
                       chromedriver_path: str
                 # total: int        # total web browser to open
                 ):
        self.path = chromedriver_path
        if not type:
            logger.warning('No web browser specify')
            return
        logger.info(f"Setting options for {type}...")
        if type.lower() == "chrome":
            from selenium.webdriver.chrome.options import Options
            self.driver = webdriver.Chrome
            # Initialize options:
            self.chrome_options = Options()
            self.chrome_options.add_argument('--start-maximized')
        # elif type.lower() == "firefox":
        #     self.driver = webdriver.Firefox
        #     # TODO: add options for firefox
        else:
            logger.error(f"{type} is not supported")
            return
        

    def start(self):
        # Launch web browser
        logger.info("Starting web browser...")
        # NOTE: for chrome only
        try:
            if self.path:
                self.driver = self.driver(self.path, chrome_options=self.chrome_options)
            else:
                self.driver = self.driver(chrome_options=self.chrome_options)               # TODO: clean this mess

        except exceptions.WebDriverException:
            logger.error('Could not initiate web driver...')
            exit(1)

        # Load cookies if exist
        if isfile("hordes_cookies.pkl"):
            self.driver.get('https://www.google.com/')              # redirect to this website before add cookies so that if we direct back to hordes.io then we will logged in.
            logger.info("Adding cookies to browser...")
            for cookie in pickle.load(open("hordes_cookies.pkl", "rb")):
                self.driver.add_cookie(cookie)

        self.driver.get(URL)

    def quit(self):
        """
        Save cookies from session and destroy driver
        """
        # Save cookies to hordes_cookies.pkl
        logger.info("Saving cookies...")
        pickle.dump(self.driver.get_cookies(), open("hordes_cookies.pkl", "wb"))
        # Closing web browser
        self.driver.close()
        # quitting
        logger.info("Quitting driver...")
        self.driver.quit()
        exit()
