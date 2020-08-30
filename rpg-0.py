"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""
class Unit:
    def __init__(self, power, health, name):
        self.name = name
        self.power = power
        self.health = health
    
    def attack(self, target ):
        target.health -= self.power
        if target.health < 0:
            print(f'The {target.name} is dead!')

    def alive(self):
        if self.health > 0:
            alive = True
            return alive
        else:
            alive =  False
            return alive

    def print_status(self):
        print(f"Currently the {self.name} has {self.health} health and {self.power} power!")

def main():
    hero = Unit(5,10, "Hero")
    goblin = Unit(2,8, "Goblin")
    minotaur = Unit(8,15, "Minotaur")


    print("You're attacked by a goblin!")
    while hero.alive() and goblin.alive():
        hero.print_status()
        print("What do you want to do?")
        print("1. fight goblin")
        print("2. do nothing")
        print("3. check")
        print("4. flee")
        print("> ",)
        user_input = input()
        if user_input == "1":
            hero.attack(goblin)
        elif user_input == "2":
            pass
        elif user_input == "3":
            goblin.print_status()
        elif user_input == "4":
            print("Goodbye.")
            break
        else:
            print("Invalid input %r" % user_input)

        if goblin.health > 0:
            # Goblin attacks hero
            goblin.attack(hero)
            print("The goblin does %d damage to you." % goblin.power)
            

main()
