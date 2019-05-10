# <img src="https://github.com/TopKeingt/hordes.io-bots/blob/master/images/hordes-icon.svg" alt="hordes.io icon" width="30" height="30">[Hordes.io](https://hordes.io) Bots [![Codacy Badge](https://api.codacy.com/project/badge/Grade/5e506058e814499cb263b3e76f8868f4)](https://www.codacy.com/app/TopKeingt/hordes.io-bots?utm_source=github.com&utm_medium=referral&utm_content=TopKeingt/hordes.io-bots&utm_campaign=Badge_Grade)[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)![License MIT](https://img.shields.io/github/license/mashape/apistatus.svg)

Automation bot that help grinding without much help from you.

### Demonstration

[![Video Demonstration](https://img.youtube.com/vi/xRAFMiTzsn0/0.jpg)](https://youtu.be/xRAFMiTzsn0)

This short video demonstration was created before some updates like (_shaman, archer, warrior supported_ and fixed bugs)

### Features:

- Attack and defend mode
- Automatic searching for enemies
- Random move to avoid bot-like behaviours
- Automatic search for another enemy when done killed the previous enemy
- Save web browser's cookies when done
- Helpful debugging messages

### Available Characters

- [x] ![archer](https://github.com/TopKeingt/hordes.io-bots/blob/master/images/class_archer.png) **Archer** (can move around)
- [x] ![mage](https://github.com/TopKeingt/hordes.io-bots/blob/master/images/class_mage.png) **Mage** (must stay at one location)
- [x] ![shaman](https://github.com/TopKeingt/hordes.io-bots/blob/master/images/class_shaman.png) **Shaman** (must stay at one location)
- [x] ![warrior](https://github.com/TopKeingt/hordes.io-bots/blob/master/images/class_warrior.png) **Warrior** (recommend to move around)

### Prerequisites

- Python 3.x
- If you use:
  - Chrome: [install chromedriver.exe](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver#quick-installation)
  - Firefox: Coming soon...

### Installation

1. Install requirements

```
    python -m pip install -r requirements.txt
```

### Notes Before Running

1. Make sure to add chromedriver.exe in environment PATH
2. If you don't want to then specify chromedriver.exe's location before running: `python main.py --path=/path/to/chromedriver.exe`

### Notes While Running

The bot might needs your help when these below problems occur.

1. The bot sometime will try to attack far away enemies while ignore closer enemies.
2. There is a bug in the game that let the skill's execution time goes negative value and I try to take this into consideration. (don't worry, for the time being, the bot will reset itself if this happen.)

### What This Bot Can Do?

- During **attack mode**, the bot can switch between first attack skill and second attack skill if it have one.
- During **defend mode**, the bot can switch between first defend skill and second defend skill if it have one (_only turn on when bot's health is low_).
- The bot could perform **random moves**
- The bot can **find different enemy** if it's attack skills could not reach or damage the current enemy.
- The bot can **rest** for few seconds when its mana goes low.
- The bot can **automatically respawn** under the acceptance of the user.

### Running

```
    python main.py
```

Use the command below to turn on debug mode:

```
    python main.py -v
```

### Todo:

[Hordes.io Bot Todo List](https://github.com/TopKeingt/hordes.io-bots/projects/1)

### Disclaimer

- This is for education purposes and researches. It is illegal to practice using this bot for level up.
- Users will responsible for using this program with evil purposes.
- I am not responsible for your actions. :)

[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://GitHub.com/TopKeingt/)

Pull requests are welcome

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
