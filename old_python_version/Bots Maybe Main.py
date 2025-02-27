import battlebots, random

HullValue = 5

class Arena:
    def __init__(self, Bot1, Bot2):
        self.bbot1 = Bot1
        self.bbot2 = Bot2
        self.turn = 0

    def battle(self):
        self.turn = 0
        while self.bbot1.is_alive() and self.bbot2.is_alive():
            self.turn += 1
            print("Turn " + str(self.turn) + ": ")
            print()
            #begin battle round
            if self.bbot1.base_speed > self.bbot2.base_speed:
                self.bbot1.take_turn(self.bbot2)
                self.bbot2.take_turn(self.bbot1)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round")
                print("")
            elif self.bbot1.base_speed == self.bbot2.base_speed:
                e = random.randint(1, 2)
                if e == 1:
                    self.bbot2.take_turn(self.bbot1)
                    self.bbot1.take_turn(self.bbot2)
                else:
                    self.bbot1.take_turn(self.bbot2)
                    self.bbot2.take_turn(self.bbot1)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round")
                print("")
            elif self.bbot1.base_speed < self.bbot2.base_speed:
                self.bbot2.take_turn(self.bbot1)
                self.bbot1.take_turn(self.bbot2)
                self.bbot1.get_stats()
                self.bbot2.get_stats()
                input("Press enter for next round")
                print("")
        if self.bbot1.is_alive() and not self.bbot2.is_alive():
            print(self.bbot1.name + " is the winner!")
            return 1
        elif self.bbot2.is_alive() and not self.bbot1.is_alive():
            print(self.bbot2.name + " is the winner!")
            return 2
        else:
            if self.bbot1.base_speed >= self.bbot2.base_speed:
                print(self.bbot1.name + " is the winner by speed tiebreaker!")
                return 1
            else:
                print(self.bbot2.name + " is the winner by speed tiebreaker!")
                return 2

def setBattleBotStats(Bot=battlebots):
    Bot.name = input("What is your BattleBot's Name?: ")
    points_left = 20
    while(points_left != 0):
        Bot.hull = HullValue * int(input("Out of " + str(points_left) + " points, how many would you like to put into " + Bot.name + "'s Hull?")) + HullValue
        points_left -= (Bot.hull / HullValue) -HullValue
        Bot.base_armor = int(input(
            "Out of " + str(points_left) + " points, how many would you like to put into " + Bot.name + "'s armor?")) + 1
        points_left -= Bot.base_armor-1
        Bot.base_speed = int(input(
            "Out of " + str(points_left) + " points, how many would you like to put into " + Bot.name + "'s speed?")) + 1
        points_left -= Bot.base_speed-1
        Bot.base_damage = int(input(
            "Out of " + str(points_left) + " points, how many would you like to put into " + Bot.name + "'s damage?")) + 1
        points_left -= Bot.base_damage-1.
        print()
        if points_left != 0:
            if points_left < 0:
                print("You used " + str(-1 * points_left) + "too many points!")
            else:
                print("You didn't use " + str(points_left) + "points!")
            print("Please try again!")
        print("Your stats: ")
        Bot.get_stats()


def main():
    #declare both Bots for each student here
    Bot1 = battlebots.PIKUBattleBot_OLD_obsolete()
    #setBattleBotStats(Bot1)
    Bot2 = battlebots.MithranBattleBot()
    #setBattleBotStats(Bot2)
    arena = Arena(Bot1, Bot2)
    arena.battle()


if __name__ == "__main__":
    main()





