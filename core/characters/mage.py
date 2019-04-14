from core.bot import Bot
from core.setup_logger import logger
import time


class Mage(Bot):
    _skills = {
        "attack": {
            "1": {
                "key": 2,
                "name": "Frostcall",
                "Cooldown": 7,
                "MPCost": 22.4
            },
            "2": {
                "key": 1,
                "name": "Ice Bolt",
                "Cooldown": 0,
                "MPCost": 5.6
            }
        },
        "defend": {
            "1": {
                "key": 4,
                "name": "Iceblock",
                "Cooldown": 18,
                "MPCost": 33.6
            },
            "2": {
                "key": 3,
                "name": "Teleport",
                "Cooldown": 9,
                "MPCost": 22.4
            }
        }
    }
    def __init__(self, driver):
        super().__init__(driver)
        self.attack_countdown = 8
        self.defend_1_countdown = 19
        self.defend_2_countdown = 10
        self.attack_1 = self._skills["attack"].get("1")
        self.attack_2 = self._skills["attack"].get("2")
        self.defend_1 = self._skills["defend"].get("1")
        self.defend_2 = self._skills["defend"].get("2")
        
    
    def attack(self):
        if time.time() - self.attack_countdown > self.attack_1.get("Cooldown"):
            # self.attack_1     Run
            self.action.send_keys(self.attack_1.get("key"))
            self.attack_countdown = time.time()
            logger.debug("Wait for attacking skill to finish...")
            time.sleep(4)                   # The duration of the skill is 4 seconds so we wait for it to finish
        else:
            # self.attack_2     Run
            self.action.send_keys(self.attack_2.get("key"))
    
    def defend(self):
        if time.time() - self.defend_1_countdown > self.defend_1.get("Cooldown"):
            # self.defend_1     Run
            self.action.send_keys(self.defend_1.get("key"))
            self.defend_1_countdown = time.time()
            logger.debug("Wait for defending skill to finish...")
            time.sleep(5)                   # The duration of the skill is 5 seconds so we wait for it to finish
        else:
            # self.defend_2 (if exist)     Run
            if time.time() - self.defend_2_countdown > self.defend_2.get("Cooldown"):
                self.action.send_keys(self.defend_2.get("key"))
                self.defend_2_countdown = time.time()
