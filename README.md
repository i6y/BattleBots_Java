# BattleBots_Java
#### A fun, turn-based BattleBots game, where you code your own bots and pit them against others!
Here, you can find both the old Python version of the game, and the new version, in Java!
Read first how to play the game, then how to run it below.
- #### [How to play the game](#how-you-should-play-this-game-will-add-python-version-docs-l8r)
- #### [How to run the game](#how-to-run-this-game)
- #### [About this game](#a-little-about-the-history-of-this-game)
## How you should play this game (will add Python version docs l8r):
### Java Version:
- In the `/Main_Game` directory there are two bot files: `LiamBattleBot.java` and `PikuBattleBot.java` **These are two example robots to help you code your own!**.
    - **For newcomers:** It is highly suggested you check out `LiamBattleBot.java` first, as it is the most simple robot, and is a great reference for coding your own.
 
- Say you want to create it from scratch. You should begin your file as follows below:
    -  Note: Your bot **must** have the following stats (and they **must** all add up to 25 for fairness):
        - **As a string:** `this.name`
        - **As a double:** `this.hull`
        - **As a double:** `this.base_armor`
        - **As a double:** `this.base_damage`
        - **As a double:** `this.base_speed`
        - **As an integer:** `this.scrap`
          > Note: it is best to set scrap as 0, so your bot's power is all immediately usable. Scrap builds up by sacrificing/"scrapping" a number of points of a specified stat. You can then use that scrap to super upgrade other stats past their normal limits.

<details>
<summary><ins>ExampleBot.java (<strong>OPEN ME</strong>)</ins></summary>

```java
class ExampleBot extends BattleBot
{
    // The class constructor, where you define your bot's name and stats, along with extra variables and parameters that are unique to your bot.
    public BotXYZ()
    {
        this.name = "Example";
        this.hull = 5.0 * (HullValue);
        this.base_armor = 19.0;
        this.base_damage = 1.0;
        this.base_speed = 1.0;
        this.scrap = 0;
    }
    // The function where you code what the bot does. This must be titled take_turn.
    public void take_turn(BattleBot enemy)
    {
        // In this example, 'BotXYZ' uses RNG(random number generation) to decide what to do. However, the fun of it is that it's all up to you!
        // NOTE: Your bot is only able to do one move at a time. As such, program your bot in such a way that if you
        // plan to do a combo of moves, there is a placeholder variable so that it knows how far it is in the sequence, as the combo will be split into multiple turns.
        int rand = (int) (Math.random() * 100 + 1);
        if(rand < 26)
        {
            this.upgrade_hull();
        }
        else if(rand < 51)
        {
            this.attack(enemy);
        }
        else if(rand < 76)
        {
            this.upgrade_damage();
        }
        else if(rand < 101)
        {
            this.upgrade_speed();
        }
    }

  }
```
</details>

 - Now, go to `arena.java` and change `bot1` or `bot2` with your bot, as an object of type BattleBot, et voilà! Now, your bot will be in the match. Cool, right? Like training a chicken then sending it out to fight!

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
 - The minimum version of Python required to run this is **Python 3.0** 💀
 - Download the files in `/old_python_verson` in **one directory**.
 - Run `Main_Game.py`.
     - Mac (local):
       ```bash
       python3 Main_Game.py
       ```

## A little about the history of this game:
AFAIK, this game was originally created **in Python** during Summer 2022 or before for an iDTech summer camp.
The basis of this game is that you code your own robot, giving it stats and an AI that tells it what to do.
Last summer, I then backwards engineered this version and re-coded it in Python - that is what you see in `/old_python_version`.
I was recently assigned to recreate the game in Java, so here it is, in `/Main_Game`.
