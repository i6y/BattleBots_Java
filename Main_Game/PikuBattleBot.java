public class PikuBattleBot extends BattleBot
{
    private boolean superProgress;
    private boolean superMode;

    public PikuBattleBot()
    {
        this.name = "Glod";
        this.hull = 5.0 * (1*HullValue);
        this.base_armor = 18.0;
        this.base_damage = 1.0;
        this.base_speed = 1.0;
        this.scrap = 0;
    } 
    // This advanced Bot's take_turn function! It first maxes out its stats, then transitions to a "super mode" where it scraps damage, and super upgrades its hull past the limit, while simultaneously upgrading its damage to keep it maxed out.
    // Often, a match with this bot will span multiple hundreds of moves, because of the time required to do this procedure.
    public void take_turn(BattleBot enemy)
    {
        //----INITIAL UPGRADES
        // max out hull first, then other stats in order of armor, damage, then speed
        if(hull<98*5)
        {
            this.upgrade_hull();;
        }
        else
        {
            if(this.getBase_armor() < 93)
            {
                this.upgrade_armor();
            }
            else if(this.getBase_damage()<99&&!this.superMode)
            {
                this.upgrade_damage();
            }
            // for supermode (uses scrap)
            else if(this.superMode&&this.getBase_damage()<=79)
            {
                this.upgrade_damage();
            }
            else if(this.getBase_speed()<45)
            {
                this.upgrade_speed();
            }
            //-----SUPER MODE!!!!!!! scrap stats and maintain efficient moves to bring stats way past margin :D
            else if(this.getHull() < 1000)
            {
                //Starts when damage reaches its max. Scrap 20 damage repeatedly.. 99 -> 79 -> 99.. so on.
                if(this.getBase_damage()==99)
                {
                    this.superMode = true;
                    this.scrap_damage(20);
                    this.superProgress = true;
                }

                //Checks if the super is in progress (robot has scrapped 20 damag but has not yet super upgraded)
                else if(this.superMode&&this.superProgress)
                {
                    //sets superProgress ot 0 and finishes super
                    this.superProgress = false;
                    this.super_upgrade_hull();
                }

                //Checks if super is done and starts another one
                else if(this.superMode&&!this.superProgress)
                {
                    this.scrap_damage(20);
                    this.superProgress = true;
                }
            }
            //-----ATTACK!!
            else
            {
                if(this.getBase_damage() < 99)
                {
                    this.upgrade_damage();
                }
                else{
                    System.out.print("\nA cold breeze drifts through the arena..\n\n" + this.getName() + " is about to attack.\n\n");
                    this.attack(enemy);
                }
            }

        }
    }
}
