from core.bot import Bot


class Shaman(Bot):
    _skills = {
        "attack": {
            "1": {
                "key": 3,
                "name": "Decay",
                "cooldown": 0,
                "duration": 1.3,
                "MPCost": 10.2
            },
            "2": {
                "key": 2,
                "name": "Equilibrate",
                "cooldown": 0,
                "duration": 1,
                "MPCost": 20.4
            }
        },
        "defend": {
            "1": {
                "key": 1,
                "name": "Healing Ritual",
                "cooldown": 1,
                "duration": 1,
                "MPCost": 8.2
            }
        }
    }

    def __init__(self, driver):
        super().__init__(driver)
        self.attack_1 = self._skills["attack"].get("1")
        self.attack_2 = self._skills["attack"].get("2")
        self.defend_1 = self._skills["defend"].get("1")
        self.attack_1_countdown = self.attack_1.get("cooldown")
        self.defend_1_countdown = self.defend_1.get("cooldown")

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