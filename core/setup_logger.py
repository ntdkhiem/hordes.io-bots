import logging
"""
Logging levels:
    - Critical: None
    - Error: Program errors
    - Warning: Missing requirements
    - Info: Information of the program
    - Debug: workflow
:return: void
"""
# custom logger
logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')
logger = logging.getLogger('hordes.io')
# File handler
file_handler = logging.FileHandler('hordes.io.log')
file_handler.setLevel(logging.ERROR)
file_formatter = logging.Formatter('[%(asctime)s][%(filename)s][%(levelname)s] %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)

logger.info('Setting logger...')
