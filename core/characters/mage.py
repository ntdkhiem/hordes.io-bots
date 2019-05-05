from core.bot import Bot

class Mage(Bot):
    _skills = {
        "attack": {
            "1": {
                "key": 2,
                "name": "Frostcall",
                "cooldown": 7,
                "duration": 5,
            },
            "2": {
                "key": 1,
                "name": "Ice Bolt",
                "cooldown": 1,
                "duration": 0,
            }
        },
        "defend": {
            "1": {
                "key": 4,
                "name": "Iceblock",
                "cooldown": 14,
                "duration": 5,
            },
            "2": {
                "key": 3,
                "name": "Teleport",
                "cooldown": 9,
                "duration": 0,
            }
        }
    }
    def __init__(self, driver):
        super().__init__(driver)
        self.attack_1 = self._skills["attack"].get("1")
        self.attack_2 = self._skills["attack"].get("2")
        self.defend_1 = self._skills["defend"].get("1")
        self.defend_2 = self._skills["defend"].get("2")
        self.attack_1_countdown = self.attack_1.get("cooldown")
        self.defend_1_countdown = self.defend_1.get("cooldown")
        self.defend_2_countdown = self.defend_2.get("cooldown")


    def attack(self):
            if self.get_cooldown_elapsed(self.attack_1_countdown) > self.attack_1.get("cooldown"):
                # self.attack_1     Run
                self.cast(self.attack_1)
                self.attack_1_countdown = self.set_time()
            else:
                # self.attack_2     Run
                self.cast(self.attack_2)

    def defend(self):
            if self.get_cooldown_elapsed(self.defend_1_countdown) > self.defend_1.get("cooldown"):
                # self.defend_1     Run
                self.cast(self.defend_1)
                self.defend_1_countdown = self.set_time()
            else:
                # self.defend_2     Run
                if self.get_cooldown_elapsed(self.defend_2_countdown) > self.defend_2.get("cooldown"):
                    self.cast(self.defend_2)
                    self.defend_2_countdown = self.set_time()
