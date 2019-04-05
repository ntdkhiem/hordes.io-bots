from core.bot import Bot
import time


class Mage(Bot):
    def __init__(self, driver):
        super().__init__(driver)

    def run(self):
        while True:
            try:
                super().run()
                print('MAGE RUNNING...')
                time.sleep(5)
            except KeyboardInterrupt:
                self.quit()
