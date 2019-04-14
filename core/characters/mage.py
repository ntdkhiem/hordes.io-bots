from core.bot import Bot


class Mage(Bot):
    def __init__(self, driver):
        super().__init__(driver)
    
    def attack(self):
        print('Attacking...')
    
    def heal(self):
        print('Healing...')
