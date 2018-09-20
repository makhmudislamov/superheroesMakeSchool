import random

class Ability:
    def __init__(self, name, attack_strength):
        self.name = name
        self.attack_strength = int(attack_strength)

    def attack(self):
            low_attack_strength = self.attack_strength // 2
            return random.randint(low_attack_strength, self.attack_strength)

    def update_attack(self, attack_strength):
        self.attack_strength = attack_strength

class Hero:
    def __init__(self, name, health=100):
        # Initialize starting values
        self.abilities = []
        self.name = name
        self.armors = list()
        self.start_health = health
        self.health = health
        self.deaths = 0
        self.kills = 0

    def add_ability(self, ability):
        # Add ability to abilities list
        self.abilities.append(ability)
       

    def attack(self):
          # Call the attack method on every ability in our ability list
          # Add up and return the total of all attacks
        for ability in self.abilities:
            return ability.attack()

    def defend(self):
        """
        This method should run the defend method on each piece of armor and calculate the total defense. 

        If the hero's health is 0, the hero is out of play and should return 0 defense points.
        """
        if self.health == 0:
            print("We lost a hero!")
            return 0
        else:
            if self.armors:
                for i in self.armors:
                    return i.defend()
            else:
                return 0


    def take_damage(self, damage_amt):
        """
        This method should subtract the damage amount from the 
        hero's health. 

        If the hero dies update number of deaths.
        """
        self.health -= damage_amt
        if self.health < 1:
            print("A Hero has fallen!", self.name)
            self.deaths += 1

    def add_kill(self, num_kills):
        """
        This method should add the number of kills to self.kills
        """
        print("Killed!")
        self.kills += num_kills


class Weapon(Ability):
    def attack(self):
        """
        This method should should return a random value
        between 0 and the full attack power of the weapon.
        Hint: The attack power is inherited.
        """
        return random.randint(0, self.attack_strength)


class Team:
    def init(self, team_name):
        """Instantiate resources."""
        self.name = team_name
        self.heroes = list()

    def add_hero(self, Hero):
        """Add Hero object to heroes list."""
        self.heroes.append(Hero)

    def remove_hero(self, name):
        if Hero in self.heroes:
            self.heroes.pop(Hero)
        else:
            return 0

    def find_hero(self, name):
        if Hero in self.heroes:
            return Hero
        else:
            return 0

    def view_all_heroes(self):
        """Print out all heroes to the console."""
        print(len(self.heroes))

    def attack(self, other_team):
        """
        This method should total our teams attack strength and call the defend() method on the rival team that is passed in.

        It should call add_kill() on each hero with the number of kills made.
        """
        # REVISIT
        sum = 0
        for i in self.heroes:
            sum += i.attack()
            if i.weapons != None:
                for n in i.weapons:
                    sum += n.attack()
        for i in other_team.heroes:
            sum -= i.defend()
        if sum > 0:
            other_team.deal_damage(sum)
            for i in other_team.heroes:
                if i.deaths > 0:
                    for v in self.heroes:
                        v.kills += i.deaths
        else:
            return sum

    def defend(self, damage_amt):
        """
        This method should calculate our team's total defense.
        Any damage in excess of our team's total defense should be evenly distributed amongst all heroes with the deal_damage() method.

        Return number of heroes killed in attack.
        """
        sum = 0
        for i in self.heroes:
            sum += i.defend()
        return sum

    def deal_damage(self, damage):
        """
        Divide the total damage amongst all heroes.
        Return the number of heros that died in attack.
        """
        ndamage = damage // len(self.heroes)
        for i in self.heroes:
            i.take_damage(ndamage)

    def revive_heroes(self, health=100):
        """
        This method should reset all heroes health to their
        original starting value.
        """
        for i in self.heroes:
            i.health = health

    def stats(self):
        """
        This method should print the ratio of kills/deaths for each member of the team to the screen. 

        This data must be output to the terminal.
        """
        for i in self.heroes:
            print(i.name, "victories", i.kills)
            print(i.name, "defeates", i.deaths)

    def update_kills(self):
        """
        This method should update each hero when there is a team kill.
        """
        for i in self.heroes:
            i.add_kill(1)


class Armor:
    def __init__(self, name, defense):
        """Instantiate name and defense strength."""
        self.name = name
        self.defense = defense

    def defend(self):
        return random.randint(0, self.defense)


class Arena:
    def __init__(self):
        """
        self.team_one = None
        self.team_two = None
        """

    def build_team_one(self):
        """
        This method should allow a user to build team one.
        """

    def build_team_two(self):
        """
        This method should allow user to build team two.
        """

    def team_battle(self):
        """
        This method should continue to battle teams until 
        one or both teams are dead.
        """

    def show_stats(self):
        """
        This method should print out the battle statistics 
        including each heroes kill/death ratio.
        """


if __name__ == "__main__":
    hero = Hero("Wonder Woman")
    print(hero.attack())
    ability = Ability("Divine Speed", 300)
    hero.add_ability(ability)
    print(hero.attack())
    new_ability = Ability("Super Human Strength", 800)
    hero.add_ability(new_ability)
    print(hero.attack())
