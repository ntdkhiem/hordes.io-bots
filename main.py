import argparse
from core.browser import Driver
from core.characters import *

__author__ = "TopKeingt"
__version__ = "0.1.0"


def parse_arguments():
    parser = argparse.ArgumentParser(description="Hordes.io bot configuration")
    parser.add_argument('--browser', '-b', required=True, help="Specific a web browser to start (chrome/firefox)")
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
    driver = Driver(args.browser).start()
    bot = mage.Mage(driver).run()


if __name__ == "__main__":
    main()


