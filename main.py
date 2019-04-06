import argparse
import logging
from core.browser import Driver
from core.characters import *

__author__ = "TopKeingt"
__version__ = "0.0.4"


def parse_arguments():
    parser = argparse.ArgumentParser(description="Hordes.io bot configuration")
    parser.add_argument('--browser', '-b', help="Specific a web browser to start (chrome/firefox)")
    # arg.add_argument('--character', '-c', default=1, type=int, help="Amount of character to play at once")
    _args = parser.parse_args()
    return _args


def banner():
    print('''.----.  .---. .-----. .----. 
| {_} }/ {-. \`-' '-'{ {__-` 
| {_} }\ '-} /  } {  .-._} } 
`----'  `---'   `-'  `----'  
                             @TopKeingt''')


def init_logging():
    """
    Logging levels:
        - Critical:
        - Error:
        - Warning:
        - Info:
        - Debug:
    :return: void
    """
    # custom logger
    logger = logging.getLogger('hordes.io')
    # handlers
    stream_handler = logging.StreamHandler()
    file_handler = logging.FileHandler('hordes.io.log')
    # default mode
    stream_handler.setLevel(logging.INFO)
    file_handler.setLevel(logging.ERROR)
    # formatters
    stream_formatter = logging.Formatter('[%(levelname)s] %(message)s')
    file_formatter = logging.Formatter('[%(asctime)s][%(filename)s][%(levelname)s] %(message)s')

    stream_handler.setFormatter(stream_formatter)
    file_handler.setFormatter(file_formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)
    logger.info('Setting logger...')


def main():
    banner()
    args = parse_arguments()
    init_logging()
    driver = Driver(args.browser).start()
    bot = mage.Mage(driver).run()


if __name__ == "__main__":
    main()


