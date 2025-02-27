public class LiamBattleBot extends BattleBot 
{
    public LiamBattleBot()
    {
        this.name = "Someone's Robot";
        this.hull = 10.0 * (1*HullValue);
        this.base_armor = 7.0;
        this.base_damage = 7.0;
        this.base_speed = 1.0;
        this.scrap = 0;
    }
    public void take_turn(BattleBot enemy)
    {
        int rand = (int) (Math.random() * 10 + 1);
        if(this.hull < 10 && this.getBase_armor() > 0)
        {
            this.scrap_armor((int) this.getBase_armor());
        }
        else if(this.getHull() < 10 && this.getScrap() > 0)
        {
            this.super_upgrade_hull();
        }
        else if(rand < 7)
        {
            this.upgrade_speed();
        }
        else if(rand<8)
        {
            this.attack(enemy);
        }
        else if(rand<9)
        {
            this.upgrade_damage();
        }
        else if(rand < 10)
        {
            this.upgrade_speed();
        }
        
    }
}
