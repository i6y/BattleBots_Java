import random


# -------------- DEFAULT VALUES!
NoMove = 0
Attack = 1
UpgradeHull = 2
UpgradeArmor = 3
UpgradeDamage = 4
UpgradeSpeed = 5
ScrapHull = 6
ScrapArmor = 7
ScrapDamage = 8
ScrapSpeed = 9
SuperUpgradeHull = 10
SuperUpgradeArmor = 11
SuperUpgradeDamage = 12
SuperUpgradeSpeed = 13


HullValue = 5

class BattleBot:

    def __init__(self):
        self.name = "ROB" + str(random.randrange(10))
        self.base_armor = 3.0 + 1.0
        self.base_damage = 5.0 + 1.0
        self.base_speed = 2.0 + 1.0
        self.hull = 10 * HullValue + (1 * HullValue)
        self.scrap = 0
        self.last_move = NoMove


    def reset_stats(self):
        self.name = "ROB" + str(random.randrange(10))
        self.hull = 10 * HullValue + (1 * HullValue)
        self.base_armor = 3.0 + 1.0
        self.base_damage = 5.0 + 1.0
        self.base_speed = 2.0 + 1.0
        self.scrap = 0
        self.last_move = NoMove

    def attack(self, enemy):
        damage_dealt = self.base_damage - (self.base_damage * enemy.base_armor / 100)
        print(self.name + " attacked " + enemy.name + " for " + str(damage_dealt) + " damage!")
        r = random.randrange(100)
        if r < enemy.base_speed * 2:
            if enemy.base_speed <= 5:
                print("AGAINST ALL ODDS: " + enemy.name + " DODGED THE ATTACK!!!")
            else:
                print(enemy.name + " DODGED THE ATTACK!!!")
        else:
            enemy.take_damage(damage_dealt)
        self.last_move = Attack

    def take_damage(self, damage_dealt):
        self.hull -= damage_dealt

#add colored text
#add timing system
    def get_stats(self):
        power_level = self.hull/10 + self.base_damage + self.base_speed + self.base_armor
        potential_power_level = power_level + self.scrap
        print()
        print(self.name + "'s Current Power Level: " + str(power_level) + " | Potential Power Level: " + str(potential_power_level))
        print(" Stats |Hull: " + str(self.hull) + "| Armor: " + str(self.base_armor) + "| Damage: " + str(self.base_damage) + "| Speed: " + str(self.base_speed) + "| Scrap: " + str(self.scrap))
        print()

    def is_alive(self):
        if self.hull <= 0.0 or self.base_speed <= 0.0 or self.base_armor <= 0.0 or self.base_damage <= 0.0:
            return False
        else:
            return True

    def upgrade_damage(self):
        if self.base_damage <= 100 - 2:
            self.base_damage += 2
            print(self.name + " upgraded their damage +2 to " + str(self.base_damage))
        else:
            print(self.name + " attempted to upgrade their damage +2, but they already have " + str(self.base_damage) + " damage!")
        self.last_move = UpgradeDamage

    def upgrade_speed(self):
        if self.base_speed <= 45 - 2:
            self.base_speed += 2
            print(self.name + " upgraded their speed +2 to " + str(self.base_speed))
        else:
            print(self.name + " attempted to upgrade their speed +2, but they already have " + str(self.base_speed) + " speed!")
        self.last_move = UpgradeSpeed

    def upgrade_armor(self):
        if self.base_armor <= 94 - 2:
            self.base_armor += 2
            print(self.name + " upgraded their armor +2 to " + str(self.base_armor))
        else:
            print(self.name + " attempted to upgrade their armor +2, but they already have " + str(self.base_armor) + "armor!")
        self.last_move = UpgradeArmor

    def upgrade_hull(self):
        if self.hull <= (100 * HullValue) - (2 * HullValue):
            self.hull += self.base_armor
            print(self.name + " upgraded their hull + their base armor of " + str(self.base_armor) + " to " + str(self.hull))
        else:
            print(self.name + " attempted to upgrade their hull + their base armor, but they already have " + str(self.hull) + " hull!")
        self.last_move = UpgradeHull

    def scrap_damage(self, amount=int):
        scrap_amount = amount
        if self.base_damage - scrap_amount >= 1:
            self.base_damage -= scrap_amount
            self.scrap += scrap_amount
        else:
            scrap_amount = self.base_damage - 1
            self.base_damage = 1
            self.scrap += scrap_amount
        print(self.name + " scrapped " + str(scrap_amount) + " damage to get  " + str(scrap_amount) + " scrap...")
        self.last_move = ScrapDamage


    def scrap_armor(self, amount):
        scrap_amount = amount
        if self.base_armor - scrap_amount >= 1:
            self.base_armor -= scrap_amount
            self.scrap += scrap_amount
        else:
            scrap_amount = self.base_armor - 1
            self.base_armor = 1
            self.scrap += scrap_amount
        print(self.name + " scrapped " + str(scrap_amount) + " armor to get  " + str(scrap_amount) + " scrap...")
        self.last_move = ScrapArmor

    def scrap_speed(self, amount):
        scrap_amount = amount
        if self.base_speed - scrap_amount >= 1:
            self.base_speed -= scrap_amount
            self.scrap += scrap_amount
        else:
            scrap_amount = self.base_speed - 1
            self.base_speed = 1
            self.scrap += scrap_amount
        print(self.name + " scrapped " + str(scrap_amount) + " speed to get  " + str(scrap_amount) + " scrap...")
        self.last_move = ScrapSpeed

    def scrap_hull(self, amount):
        scrap_amount = round(amount)
        if self.hull - (scrap_amount * HullValue) >= HullValue:
            self.hull -= (scrap_amount * HullValue)
            self.scrap += scrap_amount
        else:
            scrap_amount = round((self.hull - HullValue) / HullValue)
            self.hull = HullValue
            self.scrap += scrap_amount
        print(self.name + " scrapped " + str(scrap_amount * HullValue) + " hull to get  " + str(scrap_amount) + " scrap...")
        self.last_move = ScrapHull

    def super_upgrade_damage(self):
        scrap = self.scrap
        self.base_damage += self.scrap
        self.scrap = 0
        print(self.name + " SUPER UPGRADED THEIR DAMAGE WITH " + str(scrap) + " SCRAP TO " + str(self.base_damage))
        self.last_move = SuperUpgradeDamage

    def super_upgrade_speed(self):
        scrap = self.scrap
        self.base_speed += self.scrap
        self.scrap = 0
        print(self.name + " SUPER UPGRADED THEIR SPEED WITH " + str(scrap) + " SCRAP TO " + str(self.base_speed))
        self.last_move = SuperUpgradeSpeed

    def super_upgrade_armor(self):
        scrap = self.scrap
        self.base_armor += self.scrap
        self.scrap = 0
        print(self.name + " SUPER UPGRADED THEIR ARMOR WITH " + str(scrap) + " SCRAP TO " + str(self.base_armor))
        self.last_move = SuperUpgradeArmor

    def super_upgrade_hull(self):
        scrap = self.scrap
        self.hull += (self.scrap * HullValue)
        self.scrap = 0
        print(self.name + " SUPER UPGRADED THEIR HULL WITH " + str(scrap) + " SCRAP TO " + str(self.hull))
        self.last_move = SuperUpgradeHull

    def take_turn(self, enemy):
        #enemy_move = enemy.moves.po
        if enemy.base_damage * 2 > self.hull:
            self.upgrade_hull()
            return
        r = random.randrange(0, 40)
        if r < 8:
            self.attack(enemy)
        elif r < 9:
            self.upgrade_damage()
        elif r < 10:
            self.upgrade_speed()
        elif r < 11:
            self.upgrade_armor()
        elif r < 12:
            self.upgrade_hull()
        elif r < 13:
            self.scrap_damage(round(self.base_damage / 2))
        elif r < 14:
            self.scrap_speed(round(self.base_speed / 2))
        elif r < 15:
            self.scrap_armor(round(self.base_armor / 2))
        elif r < 16:
            self.scrap_hull(round(self.hull / (2 * HullValue)))
        elif r < 17:
            self.super_upgrade_damage()
        elif r < 18:
            self.super_upgrade_speed()
        elif r < 19:
            self.super_upgrade_armor()
        elif r < 20:
            self.super_upgrade_hull()
        else:
            self.attack(enemy)

class PIKUBattleBot_Undying(BattleBot):

    def __init__(self):
        self.name = "parry this filthy casual"
        self.hull = 5.0 + (1 * HullValue)
        self.base_armor = 19.0
        self.base_damage = 1.0
        self.base_speed = 1.0
        self.scrap = 0
        self.moves = [NoMove]
        self.power_level = self.hull + self.base_damage + self.base_speed + self.base_armor
        self.superMode = False
        self.superProgress = False
    def reset_stats(self):
        self.name = "don pollo"
        self.hull = 5.0 + (1 * HullValue)
        self.base_armor = 19.0
        self.base_damage = 1.0
        self.base_speed = 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def take_turn(self, enemy):
        #----------INITIAL UPGRADES
        # upgrade hull first, then other stats
        if self.hull<98*5:
         self.upgrade_hull()
        else:
            if self.base_armor < 93:
                self.upgrade_armor()

            elif self.base_damage<99 and not self.superMode:
                self.upgrade_damage()

            elif self.superMode and self.base_damage <= 79:
                self.upgrade_damage()

            elif self.base_speed < 45:
                self.upgrade_speed()

            #----------SUPER MODE (effective until over 1k health, and will prioritize upgrading damage if under 20)
            elif self.hull < 1000:
                # Super mode starts when damage reaches its max
                #   (therefore; damage wil only go from 99  to 79 to 99.. so on.)
                if self.base_damage == 99:
                    self.superMode = True
                    self.scrap_damage(20)
                    self.superProgress = True

                # Checks if the super is in progress (robot has scrapped 20 damage but has not yet super upgraded hull)
                elif self.superMode and self.superProgress:
                    # Sets superProgress to 0 and finishes super
                    self.superProgress = False
                    self.super_upgrade_hull()

                # Checks if the super is done and starts another one
                elif self.superMode and not self.superProgress:
                    self.scrap_damage(20)
                    self.superProgress = True

            #----------ATTACK
            else:
                if self.base_damage < 99:
                    self.upgrade_damage()
                else:
                    print( '\033[31m', "\nA cold breeze drifts through the arena..\n\n" + self.name + " is about to attack.\n\n")
                    self.attack(enemy)
                    if enemy.is_alive():
                        print("Critical damage!", '\033[97m')
                    if not enemy.is_alive():
                        print("Critical damage! And just like that, " + self.name + "'s opponent has been destroyed!", '\033[97m\n')

class JamesBattleBot(BattleBot):

    def __init__(self):
        self.name = "Trollinator"
        self.hull = 35.0 + (1 * HullValue)
        self.base_armor = 3.0 + 1.0
        self.base_damage = 7.0 + 1.0
        self.base_speed = 3.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def reset_stats(self):
        self.name = "Trollinator"
        self.hull = 40.0 + (1 * HullValue)
        self.base_armor = 3.0 + 1.0
        self.base_damage = 6.0 + 1.0
        self.base_speed = 3.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def take_turn(self, enemy):
        r = random.randrange(0, 14)
        if self.hull < 7:
            if r > 2:
                self.upgrade_hull()
            else:
                self.attack(enemy)
        elif self.hull < 15:
            if r > 6:
                self.upgrade_hull()
            else:
                self.attack(enemy)
        elif self.scrap > 0 and random.randint(1,5) == 5:
            if r < 6:
                self.super_upgrade_hull()
            elif r < 10:
                self.super_upgrade_damage()
            elif r < 12:
                self.super_upgrade_speed()
            elif r < 13:
                self.super_upgrade_armor()
        elif r < 7:
            self.attack(enemy)
        elif r < 9:
            self.upgrade_damage()
        elif r < 11:
            self.upgrade_speed()
        elif r < 13:
            self.upgrade_hull()
        elif r < 15:
            self.scrap_damage(3)


class PIKUBattleBot_OLD_obsolete(BattleBot):

    def __init__(self):
        self.name = "[E]"
        self.hull = 45.0 + (1 * HullValue)
        self.base_armor = 1.0
        self.base_damage = 10 + 1.0
        self.base_speed = 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def reset_stats(self):
        self.name = "[E]"
        self.hull = 45.0 + (1 * HullValue)
        self.base_armor = 3.0 + 1.0
        self.base_damage = 7.0 + 1.0
        self.base_speed = 2.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def take_turn(self, enemy):

        if self.hull < 20 and self.scrap > 0:
            self.super_upgrade_hull()
        elif self.hull < 10 and self.scrap == 0:
            self.upgrade_hull()
        elif self.hull < 15.0 and self.scrap > 1:
            self.super_upgrade_hull()
        elif self.base_damage == 11:
                self.upgrade_damage()
        else:
            self.attack(enemy)


class LiamBattleBot(BattleBot):

    def __init__(self):
        self.name = "Someone's Robot"
        self.hull = (7*HullValue) + (1 * HullValue)
        self.base_armor = 6.0 + 1.0
        self.base_damage = 6.0 + 1.0
        self.base_speed = 1.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def reset_stats(self):
        self.name = "Someone's Robot"
        self.hull = (7*HullValue) + (1 * HullValue)
        self.base_armor = 6.0 + 1.0
        self.base_damage = 6.0 + 1.0
        self.base_speed = 1.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def get_score(self, bot, enemy):
        power_level_bot = bot.hull / 10 + bot.base_damage + bot.base_speed + bot.base_armor
        power_level_enemy = enemy.hull / 10 + enemy.base_damage + enemy.base_speed + enemy.base_armor

        if not bot.is_alive():
            power_level_bot = -30
        if not enemy.is_alive():
            power_level_enemy = -30

        score = power_level_bot - power_level_enemy
        return score

    def get_outcome(self, new_bot, enemy, function):
        bot_copy = new_bot
        enemy_copy = enemy
        if function == Attack:
            enemy_copy.attack(bot_copy)
        elif function == UpgradeDamage:
            enemy_copy.upgrade_damage()
        elif function == UpgradeSpeed:
            enemy_copy.upgrade_speed()
        elif function == UpgradeArmor:
            enemy_copy.upgrade_armor()
        elif function == UpgradeHull:
            enemy_copy.upgrade_hull()

        score = self.get_score(bot_copy, enemy_copy)
        return score

    def check_outcomes(self, new_bot, enemy):
        average = 0
        average += self.get_outcome(new_bot, enemy, Attack)
        average += self.get_outcome(new_bot, enemy, UpgradeDamage)
        average += self.get_outcome(new_bot, enemy, UpgradeSpeed)
        average += self.get_outcome(new_bot, enemy, UpgradeArmor)
        average += self.get_outcome(new_bot, enemy, UpgradeHull)

        average = average / 5

        return average

    def reset_bot(self, bot):
        bot.base_damage = self.base_damage
        bot.base_armor = self.base_armor
        bot.base_speed = self.base_speed
        bot.hull = self.hull
        return bot



    def check_all_outcomes(self, enemy):
        print("\n", self.name, "thinks of all outcomes..\n")
        best_move = NoMove
        best_score = -9999
        new_enemy = BattleBot()
        new_enemy.name = "Simulated " + enemy.name + "1"
        new_enemy.base_damage = enemy.base_damage
        new_enemy.base_armor = enemy.base_armor
        new_enemy.base_speed = enemy.base_speed
        new_enemy.scrap = enemy.scrap
        new_enemy.hull = enemy.hull

        enemy_damage = new_enemy.base_damage
        enemy_armor = new_enemy.base_armor
        enemy_speed = new_enemy.base_speed
        enemy_hull = new_enemy.hull
        enemy_scrap = new_enemy.scrap

        #make new bbot with self stats
        new_bot = BattleBot()
        new_bot.name = "Simulated " + self.name + "1"
        new_bot.base_damage = self.base_damage
        new_bot.base_armor = self.base_armor
        new_bot.base_speed = self.base_speed
        new_bot.scrap = self.scrap
        new_bot.hull = self.hull
        self_damage = self.base_damage
        self_armor = self.base_armor
        self_speed = self.base_speed
        self_hull = self.hull
        self_scrap = self.scrap

        new_bot.attack(new_enemy)
        score = self.check_outcomes(new_bot, new_enemy)
        if score > best_score:
            best_score = score
            best_move = Attack

        # reset
        new_bot = self.reset_bot(new_bot)
        #reset enemy
        new_enemy.base_damage = enemy_damage
        new_enemy.base_armor = enemy_armor
        new_enemy.base_speed = enemy_speed
        new_enemy.scrap = enemy_scrap
        new_enemy.hull = enemy_hull

        new_bot.upgrade_damage()
        score = self.check_outcomes(new_bot, new_enemy)
        if score > best_score:
            best_score = score
            best_move = UpgradeDamage

        # reset
        new_bot = self.reset_bot(new_bot)
        #reset enemy
        new_enemy.base_damage = enemy_damage
        new_enemy.base_armor = enemy_armor
        new_enemy.base_speed = enemy_speed
        new_enemy.scrap = enemy_scrap
        new_enemy.hull = enemy_hull

        new_bot.upgrade_speed()
        score = self.check_outcomes(new_bot, new_enemy)
        if score > best_score:
            best_score = score
            best_move = UpgradeSpeed

        # reset
        new_bot = self.reset_bot(new_bot)
        #reset enemy
        new_enemy.base_damage = enemy_damage
        new_enemy.base_armor = enemy_armor
        new_enemy.base_speed = enemy_speed
        new_enemy.scrap = enemy_scrap
        new_enemy.hull = enemy_hull

        new_bot.upgrade_armor()
        score = self.check_outcomes(new_bot, new_enemy)
        if score > best_score:
            best_score = score
            best_move = UpgradeArmor

        # reset
        new_bot = self.reset_bot(new_bot)
        #reset enemy
        new_enemy.base_damage = enemy_damage
        new_enemy.base_armor = enemy_armor
        new_enemy.base_speed = enemy_speed
        new_enemy.scrap = enemy_scrap
        new_enemy.hull = enemy_hull

        new_bot.upgrade_hull()
        score = self.check_outcomes(new_bot, new_enemy)
        if score > best_score:
            best_score = score
            best_move = UpgradeHull

        # reset
        new_bot = self.reset_bot(new_bot)
        #reset enemy
        new_enemy.base_damage = enemy_damage
        new_enemy.base_armor = enemy_armor
        new_enemy.base_speed = enemy_speed
        new_enemy.scrap = enemy_scrap
        new_enemy.hull = enemy_hull

        return best_move, best_score

    def take_turn(self, enemy):
        function, best_score = self.check_all_outcomes(enemy)
        print("\n", self.name, "found a move with a score of", best_score,"\n")
        if function == Attack:
            self.attack(enemy)
        elif function == UpgradeDamage:
            self.upgrade_damage()
        elif function == UpgradeSpeed:
            self.upgrade_speed()
        elif function == UpgradeArmor:
            self.upgrade_armor()
        elif function == UpgradeHull:
            self.upgrade_hull()
        """r = random.randrange(0, 13)
        if r < 8:
            self.attack(enemy)
        elif r < 9:
            self.upgrade_damage()
        elif r < 10:
            self.upgrade_speed()
        elif r < 11:
            self.upgrade_armor()
        elif r < 12:
            self.upgrade_hull()"""

class MithranBattleBot(BattleBot):

    def __init__(self):
        self.name = "Stanley"
        self.hull = 40.0 + (1 * HullValue)
        self.base_armor = 4.0 + 1.0
        self.base_damage = 8.0 + 1.0
        self.base_speed = 1.0
        self.scrap = 0
        self.moves = [NoMove]
        self.dkajf = random.randrange(0, 12)
    def reset_stats(self):
        self.name = "Stanley"
        self.hull = 50.0 + (1 * HullValue)
        self.base_armor = 3.0 + 1.0
        self.base_damage = 5.0 + 1.0
        self.base_speed = 2.0 + 1.0
        self.scrap = 0
        self.moves = [NoMove]

    def take_turn(self, enemy):
        if self.hull < 10 and self.base_armor > 0:
            self.scrap_armor(self.base_armor)
        elif self.hull < 10 and self.scrap > 0:
            self.super_upgrade_hull()
        elif self.dkajf < 8:
            self.attack(enemy)
        elif self.dkajf < 9:
            self.upgrade_damage()
        elif self.dkajf < 10:
            self.upgrade_speed()
        elif self.dkajf < -1:
            self.upgrade_armor()
        elif self.dkajf < 11:
            self.upgrade_hull()