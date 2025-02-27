public class PikuBattleBot extends BattleBot
{
    private boolean superProgress;
    private boolean superMode;

    public PikuBattleBot()
    {
        this.name = "Glod";
        this.hull = 5.0 * (1*HullValue);
        this.base_armor = 19.0;
        this.base_damage = 1.0;
        this.base_speed = 1.0;
        this.scrap = 0;
    } 
    public void take_turn(BattleBot enemy)
    {
        //----INITIAL UPGRADES
        // upgrade hull first, then other stats
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
