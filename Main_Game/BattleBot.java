public class BattleBot
{
    //default values (this is not a default stat - this is a ratio used for hull-related calculations)
    //e.g. damage taken, or armor upgrades
    public final int HullValue = 5;
    public String name;
    public double base_armor;
    public double base_damage;
    public double base_speed;
    public double hull;
    public double scrap;

    //take damage
    public void take_damage(double damage){
        this.setHull(this.getHull() - damage);
    }

    //upgrade damage
    public void upgrade_damage()
    {
        if(this.getBase_damage()<= 100 - 2)
        {
            this.base_damage += 2;
            System.out.println(this.getName() + " upgraded their damage +2 to " + this.getBase_damage());
        }
        else
        {
            System.out.println(this.getName() + " attempted to upgrade their damage +2, but they already have " + this.getBase_damage());
        }
    }

    //upgrade speed
    public void upgrade_speed()
    {
        if(this.getBase_speed()<= 45 - 2)
        {
            this.base_speed += 2;
            System.out.println(this.getName() + " upgraded their speed +2 to " + this.getBase_speed());
        }
        else
        {
            System.out.println(this.getName() + " attempted to upgrade their speed +2, but they already have " + this.getBase_speed());
        }
    }

    //upgrade armor
    public void upgrade_armor()
    {
        if(this.getBase_armor()<= 94 - 2)
        {
            this.base_armor += 2;
            System.out.println(this.getName() + " upgraded their armor +2 to " + this.getBase_armor());
        }
        else
        {
            System.out.println(this.getName() + " attempted to upgrade their armor +2, but they already have " + this.getBase_armor());
        }
    }

    // upgrade hull
    public void upgrade_hull() {
        if (this.getHull() <= (100 * this.getHullValue()) - (2 * this.getHullValue())) {
            this.hull += this.base_armor;
            System.out.println(this.getName() + " upgraded their hull + their base armor of " + this.getBase_armor() + " to " + this.getHull());
        } else {
            System.out.println(this.getName() + " attempted to upgrade their hull + their base armor, but they already have " + this.getHull() + " hull!");
        }
    }

    // scrap damage
    public void scrap_damage(int amount) {
        int scrap_amount = amount;
        if (this.base_damage - scrap_amount >= 1) {
            this.base_damage -= scrap_amount;
            this.scrap += scrap_amount;
        } else {
            scrap_amount = (int) this.base_damage - 1;
            this.base_damage = 1;
            this.scrap += scrap_amount;
        }
        System.out.println(this.getName() + " scrapped " + scrap_amount + " damage to get " + scrap_amount + " scrap...");
    }

    // scrap armor
    public void scrap_armor(int amount) {
        int scrap_amount = amount;
        if (this.base_armor - scrap_amount >= 1) {
            this.base_armor -= scrap_amount;
            this.scrap += scrap_amount;
        } else {
            scrap_amount = (int) this.base_armor - 1;
            this.base_armor = 1;
            this.scrap += scrap_amount;
        }
        System.out.println(this.getName() + " scrapped " + scrap_amount + " armor to get " + scrap_amount + " scrap...");
    }

    // scrap speed
    public void scrap_speed(int amount) {
        int scrap_amount = amount;
        if (this.base_speed - scrap_amount >= 1) {
            this.base_speed -= scrap_amount;
            this.scrap += scrap_amount;
        } else {
            scrap_amount = (int) this.base_speed - 1;
            this.base_speed = 1;
            this.scrap += scrap_amount;
        }
        System.out.println(this.getName() + " scrapped " + scrap_amount + " speed to get " + scrap_amount + " scrap...");
    }

    // scrap hull
    public void scrap_hull(int amount) {
        int scrap_amount = Math.round(amount);
        if (this.hull - (scrap_amount * this.getHullValue()) >= this.getHullValue()) {
            this.hull -= (scrap_amount * this.getHullValue());
            this.scrap += scrap_amount;
        } else {
            scrap_amount = (int) Math.round((this.hull - this.getHullValue()) / this.getHullValue());
            this.hull = this.getHullValue();
            this.scrap += scrap_amount;
        }
        System.out.println(this.getName() + " scrapped " + (scrap_amount * this.getHullValue()) + " hull to get " + scrap_amount + " scrap...");
    }

    // super upgrade damage
    public void super_upgrade_damage() {
        double scrap = this.scrap;
        this.base_damage += this.scrap;
        this.scrap = 0;
        System.out.println(this.getName() + " SUPER UPGRADED THEIR DAMAGE WITH " + scrap + " SCRAP TO " + this.getBase_damage());
    }

    // super upgrade speed
    public void super_upgrade_speed() {
        double scrap = this.scrap;
        this.base_speed += this.scrap;
        this.scrap = 0;
        System.out.println(this.getName() + " SUPER UPGRADED THEIR SPEED WITH " + scrap + " SCRAP TO " + this.getBase_speed());
    }

    // super upgrade armor
    public void super_upgrade_armor() {
        double scrap = this.scrap;
        this.base_armor += this.scrap;
        this.scrap = 0;
        System.out.println(this.getName() + " SUPER UPGRADED THEIR ARMOR WITH " + scrap + " SCRAP TO " + this.getBase_armor());
    }

    // super upgrade hull
    public void super_upgrade_hull() {
        double scrap = this.scrap;
        this.hull += (this.scrap * this.getHullValue());
        this.scrap = 0;
        System.out.println(this.getName() + " SUPER UPGRADED THEIR HULL WITH " + scrap + " SCRAP TO " + this.getHull());
    }

    //attack
    public void attack(BattleBot enemy){
        double damage_dealt = this.getBase_damage() - (this.getBase_damage() * enemy.getBase_armor() / 100); // calculate damage
        System.out.println(this.getName() + " attacked " + enemy.getName() + " for " + damage_dealt + " damage!"); // print damage
        int r = (int) (Math.random() * 100); // speed and dodging mechanics
        if (r < enemy.getBase_speed() * 2){
            if(enemy.getBase_speed() < 5){
                System.out.println("AGAINST ALL ODDS: " + enemy.getName() + " DODGED THE ATTACK!!!");
            }
            else {
                System.out.println(enemy.getName() + " DODGED THE ATTACK!!!");
            }
        }
        else { 
            enemy.take_damage(damage_dealt);
        }
    }

    //get stats
    public void get_stats(){
        double power_level = this.getHull()/10 + this.getBase_damage() + this.getBase_speed() + this.getBase_armor();
        double potential_power_level = power_level + this.getScrap();
        System.out.println("\n" + this.getName() + "'s Current Power Level: " + power_level + " | Potential Power Level: " + potential_power_level);
        System.out.println(" Stats |Hull: " + this.getHull() + "| Armor: " + this.getBase_armor() + "| Damage: " + this.getBase_damage() + "| Speed: " + this.getBase_speed() + "| Scrap: " + this.getScrap());    
    }

    //taketurn placeholder
    public void take_turn(BattleBot enemy)
    {

    }

    //check if bot is alive
    public boolean is_alive()
    {
        if(this.getHull()<=0||this.getBase_speed()<=0||this.getBase_armor()<=0||this.getBase_damage()<=0)
        {
            return false;
        }
        return true;
    }
    //

    public int getHullValue() {
        return this.HullValue;
    }

    public String getName() {
        return this.name;
    }

    public double getBase_armor() {
        return this.base_armor;
    }

    public double getBase_damage() {
        return this.base_damage;
    }

    public double getBase_speed() {
        return this.base_speed;
    }

    public double getHull() {
        return this.hull;
    }

    public double getScrap() {
        return this.scrap;
    }

    public void setBase_armor(double base_armor) {
        this.base_armor = base_armor;
    }

    public void setBase_damage(double base_damage) {
        this.base_damage = base_damage;
    }

    public void setBase_speed(double base_speed) {
        this.base_speed = base_speed;
    }

    public void setHull(double hull) {
        this.hull = hull;
    }

    public void setScrap(double scrap) {
        this.scrap = scrap;
    }

}
