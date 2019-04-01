import pickle
from os.path import isfile
from abc import ABC, abstractmethod
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

URL = 'https://hordes.io'


class Bot(ABC):  # Root class
    def __init__(self):
        # Initialize options:
        chrome_options = Options()
        # Load Web Page with Disk Cache
        preferences = {'disk-cache-size': 4096}
        chrome_options.add_experimental_option('prefs', preferences)
        # Additional options
        chrome_options.add_argument('--disable-extensions')
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument('--start-maximized')
        print("[+] Setting options for chrome...")
        # Load cookies if exist
        if isfile("hordes_cookies.pkl"):
            for cookie in pickle.load(open("hordes_cookies.pkl", "rb")):
                self.driver.add_cookie(cookie)
            print("[+] Retrieve and add cookies...")
        # Launch web driver
        print("[+] Launching chrome...")
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\Kevin\Downloads\chromedriver.exe",
                                       chrome_options=chrome_options)
        self.driver.get(URL)
        print(f"[+] Opening {URL}...")
        input("\n[+] Press ENTER when you're login in and on the play screen...")
        # Get necessary components
        self.components = self.get_components()

    @abstractmethod
    def run(self):
        """
        Main loop for the bot
        """
        print('RUNNING')
        return

    def get_components(self):
        """
        Find and get all components (health bar, mana bar, info)
        :return: Dictionary of components
        """
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
        return components

    def quit(self):
        """
        Save cookies from session and destroy driver
        """
        # Save cookies to hordes_cookies.pkl
        print("[+] Saving cookies...")
        pickle.dump(self.driver.get_cookies(), open("hordes_cookies.pkl", "wb"))
        # quitting
        print("[+] Quitting driver...")
        self.driver.quit()
