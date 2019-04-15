# [Hordes.io](https://hordes.io) Bots
Automation bot that help grinding without much help from you.

Features:
- Attack and defend mode
- Automatic searching for enemies
- Random move to avoid bot-like behaviours
- Automatic search for another enemy when done killed the previous enemy
- Save web browser's cookies when done 
- Mage supported (more characters coming soon)
- Helpful debugging messages

### Prerequisites
- Python 3.x
- Pipenv    `python -m pip install pipenv`
- If you use:
    - Chrome: [install chromedriver.exe](https://github.com/SeleniumHQ/selenium/wiki/ChromeDriver#quick-installation)

### Installation
1) Install requirements
```
    python -m pipenv install
```

### Notes Before Running
1) Make sure to add chromedriver.exe in environment PATH
2) If you don't want to then specify chromedriver.exe's location before running: `python main.py --path=/path/to/chromedriver.exe`

### Notes While Running 
The bot is still in beta mode so it needs your help everytime these below problems occur.
1) Sometime it will try to attack enemies even when skills are disabled 
2) The bot sometime will try to attack far away enemies while ignore closer enemies. (the bot will go to defend mode if its health is low)
3) There is a bug in the game that let the skill's execution time goes negative value and I try to take this into consideration. (don't worry, for the time being, the bot will reset itself if this happen.)

### Running
1) Enter pipenv's shell and run
```
    pipenv shell && python main.py
```

### Todo:
[Hordes.io Bot Todo List](https://github.com/TopKeingt/hordes.io-bots/projects/1)

### Disclaimer
- This is for education purposes and researches. It is illegal to practice using this bot for level up.
- Users will responsible for using this program with evil purposes.
- I am not responsible for your actions. :) 


Pull requests are welcome
