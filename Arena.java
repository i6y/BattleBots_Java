import java.util.Scanner;
class Arena{
    private int turn;
    public static BattleBot bot1 = new PikuBattleBot();
    public static BattleBot bot2 = new LiamBattleBot();
    Scanner input = new Scanner(System.in);
    public Arena(){
    }
    public int battle(BattleBot bot1, BattleBot bot2){
        turn = 0;
        while(bot1.is_alive()&&bot2.is_alive())
        {
            turn++;
            System.out.println("Turn " + turn + ": ");
            System.out.println();
            // SPEED SYSTEM (faster moves first!)
            if(bot1.getBase_speed()>bot2.getBase_speed())
            {
                bot1.take_turn(bot2);
                bot2.take_turn(bot1);
                bot1.get_stats();
                bot2.get_stats();
                System.out.println("Press enter for next round");
                String go = input.nextLine();
            }
            // if speeds are equal
            else if(bot1.getBase_speed()==bot2.getBase_speed())
            {
                double e = Math.random();
                if(e<0.5)
                {
                    bot1.take_turn(bot2);
                    bot2.take_turn(bot1);
                    bot1.get_stats();
                    bot2.get_stats();
                    System.out.println("Press enter for next round");
                String go = input.nextLine();
                }
                else
                {
                    bot2.take_turn(bot1);
                    bot1.take_turn(bot2);
                    bot1.get_stats();
                    bot2.get_stats();
                    System.out.println("Press enter for next round");
                String go = input.nextLine();
                }
            }
            else if(bot2.getBase_speed()>bot1.getBase_speed())
            {
                bot2.take_turn(bot1);
                bot1.take_turn(bot2);
                bot1.get_stats();
                bot2.get_stats();
                System.out.println("Press enter for next round");
                String go = input.nextLine();
            }
        }
        // CHECK FOR END OF GAME (DEAD BOT)
        if(bot1.is_alive()&&!bot2.is_alive())
        {
            System.out.println(bot1.getName() + " is the winner!");
            return 1;
        }
        else if(bot2.is_alive()&&!bot1.is_alive())
        {
            System.out.println(bot2.getName() + " is the winner!");
            return 2;
        }
        // SPEED TIEBREAKER
        else
        {
            if(bot1.getBase_speed()>bot2.getBase_speed())
            {
                System.out.println(bot1.getName() + " is the winner by speed tiebreaker!");
                return 1;
            }
            else
            {
                System.out.println(bot2.getName() + " is the winner by speed tiebreaker!");
                return 2;
            }
        }
    }
}
