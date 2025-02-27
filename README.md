# BattleBots_Java
#### A fun, turn-based BattleBots game, where you code your own bots and pit them against others!
#### Here, you can find both the old Python version of the game, and the new version, in Java!
#### Read first how to play the game, then how to run it below.
- #### [How to play the game](#how-you-should-play-this-game-will-add-python-version-docs-l8r)
- #### [How to run the game](#how-to-run-this-game)
- #### [About this game](#a-little-about-the-history-of-this-game)
## How you should play this game (will add Python version docs l8r):
### Java Version:
 - In the `/Main_Game` directory there are two bot files: `LiamBattleBot.java` and `PikuBattleBot.java` **These are two example robots to help you code your own!**.
     - **For newcomers:** It is highly suggested you check out `LiamBattleBot.java` first, as it is the most simple robot, and is a great reference for coding your own.
 - Say you want to create it from scratch. You should begin your file as follows:
    - Your bot **must** have the following stats:
        - **As a string** `this.name`
        - **As a double** `this.hull`
        - **As a double** `this.base_armor`
        - **As a double** `this.base_damage`
        - **As a double** `this.base_speed`
        - **As an integer** `this.scrap`

**<ins>BotXYZ.java</ins>**
```java
class BotXYZ extends BattleBot
{
    public BotXYZ()
    {
        
    }
}
```

## How to run this game:
### Java Version (much faster and way better):
- Download the files in `/Main_Game` in **one directory**, then open that directory in the terminal.

- Once you are in the directory of the game, execute these in the terminal:
```zsh
javac *.java
java Game
```
#### If you're running this game online:
- Download all the files, then run `Game.java` (or compile Game.java then run the compiled file)
### Python Version (original, might be easier to understand):
 - Download the files in `/old_python_verson` in **one directory**.
 - Run `Bots Maybe Main.py`

## A little about the history of this game:
AFAIK, this game was originally created during Summer 2022 or before for an iDTech summer camp.
The basis of this game is that you code your own robot, giving it stats and an AI that tells it what to do.
