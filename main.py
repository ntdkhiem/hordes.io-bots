import argparse
import enum
from core.browser import Driver
from core.characters import *
from core.setup_logger import logger_init

__author__ = "TopKeingt"


class Character(enum.Enum):
    ARCHER = archer.Archer, 0
    MAGE = mage.Mage, 1
    SHAMAN = shaman.Shaman, 2
    WARRIOR = warrior.Warrior, 3


def choose_character():
    print('''
    1) {0}
    2) {1}
    3) {2}
    4) {3}
    '''.format(*[c.name for c in Character]))       # ID go according to character's enum

    _id = int(input("Choose your character (number only): "))

    for _class in Character:
        if _class.value[1] == (_id - 1):
            return _class.value[0]

    print("Please choose again...")
    choose_character()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Hordes.io bot configuration")
    parser.add_argument('--browser', '-b', default="chrome", dest="browser", help="Specific a web browser to start (chrome)")
    # arg.add_argument('--character', '-c', default=1, type=int, help="Amount of character to play at once")
    parser.add_argument('--path', default='', type=str, dest="path", help="Path to chromedriver.exe")
    parser.add_argument('--verbose', '-v', default=False, action='store_true', dest="verbose", help="Display bot's workflow")
    _args = parser.parse_args()
    return _args


def banner():
    print('''.----.  .---. .-----. .----. 
| {_} }/ {-. \`-' '-'{ {__-` 
| {_} }\ '-} /  } {  .-._} } 
`----'  `---'   `-'  `----'  
                             @TopKeingt''')


def main():
    args = parse_arguments()
    banner()
    player = choose_character()
    logger_init(args.verbose)
    driver = Driver(args.browser, args.path)
    driver.start()
    player(driver).run()

if __name__ == "__main__":
    main()
