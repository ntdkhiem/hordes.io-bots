# <img src="https://hordes.io/data/icons/hordes-icon.svg" alt="hordes.io icon" width="30" height="30">[Hordes.io](https://hordes.io) Bots [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e506058e814499cb263b3e76f8868f4)](https://www.codacy.com/app/TopKeingt/hordes.io-bots?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=TopKeingt/hordes.io-bots&amp;utm_campaign=Badge_Grade)
Automation bot that help grinding without much help from you.

### Demonstration
[![Video Demonstration](https://img.youtube.com/vi/xRAFMiTzsn0/0.jpg)](https://youtu.be/xRAFMiTzsn0)

### Features:
- Attack and defend mode
- Automatic searching for enemies
- Random move to avoid bot-like behaviours
- Automatic search for another enemy when done killed the previous enemy
- Save web browser's cookies when done 
- Mage supported (more characters coming soon)
- Helpful debugging messages

### Prerequisites
- Python 3.x
- If you use:
    - Chrome: [install chromedriver.exe](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver#quick-installation)

### Installation
1) Install requirements
```
    python -m pip install -r requirements.txt
```

### Notes Before Running
1) Make sure to add chromedriver.exe in environment PATH
2) If you don't want to then specify chromedriver.exe's location before running: `python main.py --path=/path/to/chromedriver.exe`

### Notes While Running 
The bot is still in beta mode so it needs your help everytime these below problems occur.
1) The bot sometime will try to attack far away enemies while ignore closer enemies.
2) There is a bug in the game that let the skill's execution time goes negative value and I try to take this into consideration. (don't worry, for the time being, the bot will reset itself if this happen.)

### What This Bot Can Do?
- During __attack mode__, the bot can switch between first attack skill and second attack skill if it have one.
- During __defend mode__, the bot can switch between first defend skill and second defend skill if it have one (_only turn on when bot's health is low_).
- The bot could perform __random moves__
- The bot can __find different enemy__ if it's attack skills could not reach or damage the current enemy.
- The bot can __rest__ for few seconds when its mana goes low.
- The bot can __automatically respawn__ under the acceptance of the user.

### Running
```
    python main.py
```

### Available Characters
- [X] ![archer](https://hordes.io/data/class/class_archer.png)  __Archer__
- [X] ![mage](https://hordes.io/data/class/class_mage.png)  __Mage__
- [ ] ![shaman](https://hordes.io/data/class/class_shaman.png)  __Shaman__
- [ ] ![warrior](https://hordes.io/data/class/class_warrior.png)  __Warrior__

### Todo:
[Hordes.io Bot Todo List](https://github.com/TopKeingt/hordes.io-bots/projects/1)

### Disclaimer
- This is for education purposes and researches. It is illegal to practice using this bot for level up.
- Users will responsible for using this program with evil purposes.
- I am not responsible for your actions. :) 


Pull requests are welcome
