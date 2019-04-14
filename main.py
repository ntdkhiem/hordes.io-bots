import argparse
from core.browser import Driver
from core.characters import *
from core.setup_logger import logger

__author__ = "TopKeingt"


def choose_character():
    characters = [
        archer.Archer,
        mage.Mage,
        shaman.Shaman,
        warrior.Warrior,
    ]
    print('''
    1) Archer (not yet implement)
    2) Mage 
    3) Shaman (not yet implement)
    4) Warrior (not yet implement)
    ''')
    _id = int(input("Choose your character (number only): "))
    if _id < len(characters):
        return characters[_id - 1]
    else:
        choose_character()


def parse_arguments():
    parser = argparse.ArgumentParser(description="Hordes.io bot configuration")
    parser.add_argument('--browser', '-b', default="chrome", help="Specific a web browser to start (chrome/firefox)")
    # arg.add_argument('--character', '-c', default=1, type=int, help="Amount of character to play at once")
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
    driver = Driver(args.browser)
    driver.start()
    bot = player(driver).run()

if __name__ == "__main__":
    main()


