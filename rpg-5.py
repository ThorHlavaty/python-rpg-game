"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's hp wherease a sword will add 2 power.
"""
import random
import time

art_assets = {
"store" : r"""
                                                     ___
                                             ___..--'  .`.
                                    ___...--'     -  .` `.`.
                           ___...--' _      -  _   .` -   `.`.
                  ___...--'  -       _   -       .`  `. - _ `.`.
           __..--'_______________ -         _  .`  _   `.   - `.`.
        .`    _ /\    -        .`      _     .`__________`. _  -`.`.
      .` -   _ /  \_     -   .`  _         .` |  Markov's |`.   - `.`.
    .`-    _  /   /\   -   .`        _   .`   |___________|  `. _   `.`.
  .`________ /__ /_ \____.`____________.`     ___       ___  - `._____`|
    |   -  __  -|    | - |  ____  |   | | _  |   |  _  |   |  _ |
    | _   |  |  | -  |   | |.--.| |___| |    |___|     |___|    |
    |     |--|  |    | _ | |'--'| |---| |   _|---|     |---|_   |
    |   - |__| _|  - |   | |.--.| |   | |    |   |_  _ |   |    |
 ---``--._      |    |   |=|'--'|=|___|=|====|___|=====|___|====|
 -- . ''  ``--._| _  |  -|_|.--.|_______|_______________________|
`--._           '--- |_  |:|'--'|:::::::|:::::::::::::::::::::::|
_____`--._ ''      . '---'``--._|:::::::|:::::::::::::::::::::::|
----------`--._          ''      ``--.._|:::::::::::::::::::::::|
`--._ _________`--._'        --     .   ''-----..............LGB'
     `--._----------`--._.  _           -- . :''           -    ''
          `--._ _________`--._ :'              -- . :''      -- . ''
 -- . ''       `--._ ---------`--._   -- . :''
          :'        `--._ _________`--._:'  -- . ''      -- . ''
  -- . ''     -- . ''    `--._----------`--._      -- . ''     -- . ''
                              `--._ _________`--._
 -- . ''           :'              `--._ ---------`--._-- . ''    -- . ''
          -- . ''       -- . ''         `--._ _________`--._   -- . ''
:'                 -- . ''          -- . ''  `--._----------`--._
""",

"Rogue" : r"""
                                     __________.__             __________                             
                                    \__    ___/|  |__   ____   \______   \ ____   ____  __ __   ____  
                                      |    |   |  |  \_/ __ \   |       _//  _ \ / ___\|  |  \_/ __ \ 
                                      |    |   |   Y  \  ___/   |    |   (  <_> ) /_/  >  |  /\  ___/ 
                                      |____|   |___|  /\___  >  |____|_  /\____/\___  /|____/  \___  >
                                                    \/     \/          \/      /_____/             \/ 
                 
                                                          __.------.                          
                                                         (__  ___   )                         
                                                            .)e  )\ /                          
                                                           /_.------                           
                                                           _/_    _/                           
                                                       __.'  / '   `-.__                       
                                                      / <.--'           `\                     
                                                     /   \   \c           |                    
                                                    /    /    )  GoT  x    \                   
                                                    |   /\    |c     / \.-  \                  
                                                    \__/  )  /(     (   \   <>'\               
                                                         / _/ _\-    `-. \/_|_ /<>             
                                                        / /--/,-\     _ \     <>.`.            
                                                        \/`--\_._) - /   `-/\    `.\           
                                                        /        `.     /   )     `\          
                                                        \      \   \___/----'                 
                                                        |      /    `(                        
                                    ___________         \    ./\_   _ \                       
                                    ______________      /     |  )    '|                      
                                    __________________ |     /   \     \     ___________a:f   
                                                      /     |     |____.)                     
                                                     /      \  a88a\___/88888a.               
                                                     \_      :)8888888888888888888a.           
                                                     /` `-----'  `Y88888888888888888            
                                                     \____|         `88888888888P'
                                                    """,
"Goblin" : r"""
             ,@@@@@@,
           ,@@@@@""@@, (     
           @@@@@ 6.6\@ :\   
           @@@C  _-_)@ : \                 
            @@@) (@@'  :  \                      
              /   \---.:.__\_                  
             ( ,   \---:---._)                 
             ; \  \|_.-;====I======{>
             |  \  _.-':   /
             |   `"/   :  / 
            //   \/    : /
            \\_   \    :/
              \ \  |   (
               ) ) )
              / / / 
       jgs   / / /_
            (_(____)
             
___________.__               ________      ___.   .__  .__                                
\__    ___/|  |__   ____    /  _____/  ____\_ |__ |  | |__| ____         ___  ________    
  |    |   |  |  \_/ __ \  /   \  ___ /  _ \| __ \|  | |  |/    \        \  \/ /  ___/    
  |    |   |   Y  \  ___/  \    \_\  (  <_> ) \_\ \  |_|  |   |  \        \   /\___ \     
  |____|   |___|  /\___  >  \______  /\____/|___  /____/__|___|  /         \_//____  > /\ 
                \/     \/          \/           \/             \/                  \/  \/ 

                """,

"Fighter" : r"""
                                    ___________.__             ___________.__       .__     __                
                                    \__    ___/|  |__   ____   \_   _____/|__| ____ |  |___/  |_  ___________ 
                                      |    |   |  |  \_/ __ \   |    __)  |  |/ ___\|  |  \   __\/ __ \_  __ \
                                      |    |   |   Y  \  ___/   |     \   |  / /_/  >   Y  \  | \  ___/|  | \/
                                      |____|   |___|  /\___  >  \___  /   |__\___  /|___|  /__|  \___  >__|   
                                                    \/     \/       \/      /_____/      \/          \/    
                 

                                                            ,dM
                                                            dMMP
                                                        dMMM'
                                                        \MM/
                                                        dMMm.
                                                        dMMP'_\---.
                                                        _| _  p ;88;`.
                                                    ,db; p >  ;8P|  `.
                                                    (``T8b,__,'dP |   |
                                                    |   `Y8b..dP  ;_  |
                                                    |    |`T88P_ /  `\;
                                                    :_.-~|d8P'`Y/    /
                                                    \_   TP    ;   7`\
                                            ,,__        >   `._  /'  /   `\_
                                            `._ '''~~~~------|`\;' ;     ,'
                                                ~~~-----~~~'\__[|;' _.-'  `\
                                                    ;--..._     .-'-._     ;
                                                    /      /`~~"'   ,'`\_ ,/
                                                    ;_    /'        /    ,/
                                                    | `~-l         ;    /
                                                    `\    ;       /\.._|
                                                    \    \      \     \
                                                    /`---';      `----'
                                                    (     /            fsc
                                                    `---'
                                                    """,

"Wizard" : r"""
                    ____ 
                  .'* *.'
               __/_*_*(_
              / _______ \
             _\_)/___\(_/_ 
            / _((\- -/))_ \
            \ \())(-)(()/ /
             ' \(((()))/ '
            / ' \)).))/ ' \
           / _ \ - | - /_  \
          (   ( .;''';. .'  )
          _\"__ /    )\ __"/_
            \/  \   ' /  \/
             .'  '...' ' )
              / /  |  \ \
             / .   .   . \
            /   .     .   \
           /   /   |   \   \
         .'   /    b    '.  '.
     _.-'    /     Bb     '-. '-._ 
 _.-'       |      BBb       '-.  '-. 
(________mrf\____.dBBBb.________)____)
 
___________.__              __      __.__                         .___                        
\__    ___/|  |__   ____   /  \    /  \__|____________ _______  __| _/       ___  ________    
  |    |   |  |  \_/ __ \  \   \/\/   /  \___   /\__  \\_  __ \/ __ |        \  \/ /  ___/    
  |    |   |   Y  \  ___/   \        /|  |/    /  / __ \|  | \/ /_/ |         \   /\___ \     
  |____|   |___|  /\___  >   \__/\  / |__/_____ \(____  /__|  \____ |          \_//____  > /\ 
                \/     \/         \/           \/     \/           \/                  \/  \/ 

                """,
"Sorcerer": r"""
                                    ___________.__               _________                                               
                                    \__    ___/|  |__   ____    /   _____/ ___________   ____  ___________   ___________ 
                                      |    |   |  |  \_/ __ \   \_____  \ /  _ \_  __ \_/ ___\/ __ \_  __ \_/ __ \_  __ \
                                      |    |   |   Y  \  ___/   /        (  <_> )  | \/\  \__\  ___/|  | \/\  ___/|  | \/
                                      |____|   |___|  /\___  > /_______  /\____/|__|    \___  >___  >__|    \___  >__|   
                                                    \/     \/          \/                   \/    \/            \/       
                                                       
                                                          \'/
                                                        -= * =-
                                                    .-"-. / #,_
                                                   / /\_ \  `#|\
                                                  / /')'\ \  /#/
                                                 (  \ = /  )/\/#
                                                  )  ) (  (/  \
                                                  (_.;`"`;._)  |
                                                / (  \|/  )   |
                                               /  /\-'^'-/\   |
                                               |  \|)=@=(  \_/
                                               |  /\/    \
                                               | /\ \     ;
                                               \(// /'    |
                                                  \/      |
                                                  |     / /
                                                  | ___/\_\
                                                  |/ / \ \|
                                                 / | | | | \
                                                 \_|/   \|_/
                                             jgs  / \`-'/ \
                                                  `-'   '-`
              """, "Zombie" : r"""
                 .....            
                C C  /            
               /<   /             
 ___ __________/_#__=o             
/(- /(\_\________   \              
\ ) \ )_      \o     \             
/|\ /|\       |'     |             
              |     _|             
             /o   __\             
            / '     |             
           / /      |             
          /_/\______|             
        (   _(    <              
         \    \    \             
          \    \    |            
           \____\____\           
            ____\_\__\_\          
           /`   /`     o\          
           |___ |_______|
            .. . b'ger 
___________.__             __________            ___.   .__                          
\__    ___/|  |__   ____   \____    /____   _____\_ |__ |__| ____   ___  ________    
  |    |   |  |  \_/ __ \    /     //  _ \ /     \| __ \|  |/ __ \  \  \/ /  ___/    
  |    |   |   Y  \  ___/   /     /(  <_> )  Y Y  \ \_\ \  \  ___/   \   /\___ \     
  |____|   |___|  /\___  > /_______ \____/|__|_|  /___  /__|\___  >   \_//____  > /\ 
                \/     \/          \/           \/    \/        \/            \/  \/ 
"""            
            }

class Character(object):
    is_playable = True
    can_cast = False
    has_magic_weapon = False
    has_wand = False
    has_torch = True
    has_shield = False
    is_poisoned = False
    on_fire = False
    def __init__(self):
        self.name = '<undefined>'
        self.hp = 1
        self.coins = 20
        self.power = 6
        self.strength = 0
        self.dex = 0
        self.con = 0
        self.intel = 0
        self.wis = 0
        self.cha = 0
        self.dam_mod = 0
        self.ac = 0
        self.proficency = 2
        self.art = art_assets[self.name]
        self.death_quote = ""

    def alive(self):
        return self.hp > 0

    def attack(self, enemy):
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
        print(f"The {self.name} rolls a {attack_roll}!")
        if attack_roll - self.dam_mod - self.proficency == 20:
            print("Wow! Critical hit!")
            enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod))
            time.sleep(1.5)
        elif attack_roll >= enemy.ac:
            enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
            time.sleep(1.5)
        else:
            print(f"{self.name.capitalize()} misses!")
            time.sleep(1.5)
    
    def throw_torch(self, enemy):
        if self.has_torch == False:
            print("Alas! You have no torch!")
        else:
            print(f"You hurl your torch at the {enemy.name}!\nThey catch ablaze!")
            enemy.on_fire = True
            self.has_torch = False
            return enemy.on_fire



    def receive_damage(self, points, attack_roll):
        self.hp -= points
        print("%s received %d damage." % (self.name, points))
        time.sleep(1.5)
        if self.hp <= 0:
            print("%s" % self.death_quote)

    def print_status(self):
        print("%s has %d health." % (self.name, self.hp))

class Fighter(Character):
    def __init__(self):
        self.name = 'Fighter'
        self.max_hp = 13
        self.hp = 13
        self.coins = 20
        self.power = 8
        self.strength = 16
        self.dex = 1
        self.con = 5
        self.intel = 8
        self.wis = 0
        self.cha = 8
        self.dam_mod = 3
        self.ac = 18
        self.proficency = 2
        self.art = art_assets[self.name]
        self.max_spells = 0
        self.death_quote = "The fighter tries to gather the courage to fight, but alas, falls for good."

    def attack(self, enemy):
        if self.is_poisoned:
            print(f"Poison courses through the {self.name}'s veins, dealing 1 damage!")
            self.hp -= 1
        if not self.alive():
            return
        while True:
            what_to_do = input("Would you like to use a [1]swift attack, or a [2]bold one? ")
            if what_to_do == "1":
                print("%s attacks %s" % (self.name, enemy.name))
                attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                print(f"The {self.name} rolls a {attack_roll}!")
                if attack_roll - self.dam_mod - self.proficency > 18:
                    print("Wow! Critical hit!")
                    enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                elif attack_roll >= enemy.ac:
                    enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                else:
                    print(f"{self.name.capitalize()} misses!")
                    time.sleep(1.5)
            if what_to_do == "2":
                print(f"The figheter lauches a savage attack at the {enemy.name}.")
                attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                print(f"The {self.name} rolls a {attack_roll}!")
                if attack_roll - self.dam_mod - self.proficency > 18:
                    print("Wow! Critical hit!")
                    enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                elif attack_roll >= enemy.ac:
                    enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                else:
                    print(f"{self.name.capitalize()} misses!")
                    time.sleep(1.5)




    def restore(self):
        self.hp = 10
        print("Fighter's heath is restored to %d!" % self.hp)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)



class Rogue(Character):
    def __init__(self):
        self.name = 'Rogue'
        self.hp = 10
        self.max_hp = 10
        self.coins = 20
        self.min_power = 1
        self.power = 6
        self.strength = 0
        self.dex = 5
        self.con = 2
        self.intel = 0
        self.wis = 1
        self.cha = 0
        self.dam_mod = 3
        self.ac = 15
        self.proficency = 2
        self.turn_counter = 0
        self.art = art_assets[self.name]
        self.max_spells = 0

    def attack(self, enemy):
        if self.is_poisoned:
            print(f"Poison courses through the {self.name}'s veins, dealing 1 damage!")
            self.hp -= 1
        if not self.alive():
            return
        if self.turn_counter == 0:
            print("%s attacks %s" % (self.name, enemy.name))
            print("The rogue launches a sneaky strike!")
            attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
            attack_roll2 = random.randint(1,20) + self.dam_mod + self.proficency
            if attack_roll2 > attack_roll:
                attack_roll = attack_roll2
            print(f"The {self.name} rolls a {attack_roll}!")    
            if attack_roll - self.dam_mod - self.proficency == 20:
                print("Wow! Critical hit!")
                enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (random.randint(1, self.power)) + (random.randint(1, self.power)) + self.dam_mod, attack_roll) 
                time.sleep(1.5)
                self.turn_counter +=1
                if enemy.hp < 1:
                    self.turn_counter = 0
            elif attack_roll >= enemy.ac:
                enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                self.turn_counter +=1
                if enemy.hp < 1:
                    self.turn_counter = 0
                time.sleep(1.5)

            else:
                print(f"{self.name.capitalize()} misses!")
                time.sleep(1.5)
                self.turn_counter +=1
                
        else: 
            while True:
                what_to_do = input("Would you like to [1]attack, or [2]focus? ")
                if what_to_do == "1":
                    print(f"The Rogue attack the {enemy.name}.")
                    attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                    print(f"The {self.name} rolls a {attack_roll}!")
                    if attack_roll - self.dam_mod - self.proficency == 20:
                        print("Wow, a critical hit!")
                        enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                        time.sleep(1.5)
                        self.turn_counter +=1
                        if enemy.hp < 1:
                            self.turn_counter = 0
                        return
                    elif attack_roll >= enemy.ac:
                        enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                        time.sleep(1.5)
                        self.turn_counter +=1
                        if enemy.hp < 1:
                            self.turn_counter = 0
                        time.sleep(1.5)
                        return
                    else:
                        print(f"{self.name.capitalize()} misses!")
                        time.sleep(1.5)
                        return
                elif what_to_do == "2":
                    print("The rogue prepares for his next strike.")
                    self.turn_counter = 0
                    return
                else:
                    print("Sorry! Didn't catch that!")
                

    def receive_damage(self, points, attack_roll):
       # if points % 2 == 0:
        self.hp -= points//2
        print("An uncanny dodge from the rogue!")
        print("%s received %d damage." % (self.name, points//2))
        if self.hp <= 0:
            print("The Rogue's luck has finally run out.")
        # else:
        #     self.hp -= (points - 1)/2
        #     print("An uncanny dodge from the rogue!")
        #     print("%s received %d damage." % (self.name, (points-1)/2))
        #     if self.hp <= 0:
        #         print("The Rogue's luck has finally run out.")

    def restore(self):
        self.hp = 10
        print("Rogues's heath is restored to %d!" % self.hp)
        time.sleep(1)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)


class Sorcerer(Character):
    can_cast = True
    def __init__(self):
        self.name = 'Sorcerer'
        self.max_hp = 7
        self.hp = 7
        self.minpower = 1
        self.power = 4
        self.coins = 20
        self.strength = 10
        self.dex = 2
        self.con = 2
        self.intel = 8
        self.wis = 4
        self.cha = 8
        self.dam_mod = 1
        self.raw_ac = 14
        self.ac = 14
        self.proficency = 2
        self.turn_counter = 0
        self.max_spells = 4
        self.spells = 4
        self.spell_power = 0
        self.art = art_assets[self.name]
        self.spell_list = ["Firebolt", "Charm", "Mage Armor", "Shield"]
        self.maxac = self.raw_ac + 4

    def attack(self, enemy):
        if self.is_poisoned:
            print(f"Poison courses through the {self.name}'s veins, dealing 1 damage!")
            self.hp -= 1
        if self.hp < 1:
            return
        while True:
            if self.spells == 0:
                print("The sorcerer is out of spells!\nThe sorcerer brandishes a dagger.")
                print("%s attacks %s" % (self.name, enemy.name))
                attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                print(f"The {self.name} rolls a {attack_roll}!")
                if attack_roll - self.dam_mod - self.proficency == 20:
                    print("Wow! Critical hit!")
                    enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                elif attack_roll >= enemy.ac:
                    enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                else:
                    print(f"{self.name.capitalize()} misses!")
                    time.sleep(1.5)
                    break
            what_to_do = input("Would you like to use your [1]dagger, or a [2]spell? ")
            if what_to_do == "1":
                print("%s attacks %s" % (self.name, enemy.name))
                attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                print(f"The {self.name} rolls a {attack_roll}!")
                if attack_roll - self.dam_mod - self.proficency == 20:
                    print("Wow! Critical hit!")
                    enemy.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                    break
                elif attack_roll >= enemy.ac:
                    enemy.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                    break
                else:
                    print(f"{self.name.capitalize()} misses!")
                    time.sleep(1.5)
                    break
            elif what_to_do == "2":
                while True:
                    number = 0
                    print("Your spells are:")
                    for spell in self.spell_list:
                        number += 1
                        print(str(number) + ". " + spell)
                    if self.spells == 1:
                        spell_select = int(input(f"You have {self.spells} spell slot left. What spell would you like to cast? ")) - 1
                    else:
                        spell_select = int(input(f"You have {self.spells} spell slots left. What spell would you like to cast? ")) - 1
                    if self.spell_list[spell_select] == "Firebolt":
                            print("A beam of fire shoots from your fingertips!")
                            dex_save = enemy.dex + random.randint(1,20) - self.spell_power
                            self.spells -= 1
                            print(f"The {enemy.name} rolls a {dex_save}")
                            if dex_save > 12 and dex_save < 15:
                                damage_roll = random.randint(1,6) + self.spell_power
                                print(f"The {enemy.name} barely jumps out of the way! You singe them, dealing {damage_roll}.")
                                enemy.hp -= damage_roll
                                enemy.on_fire = True
                                time.sleep(1.5)
                                return
                            elif dex_save < 12:
                                damage_roll = random.randint(1,6) + random.randint(1,6) + self.spell_power
                                print(f"The {enemy.name} is engulfed in flames, causing {damage_roll} damage!")
                                enemy.hp -= damage_roll
                                enemy.on_fire = True
                                time.sleep(1.5)
                                return
                            else:
                                print(f"The {enemy.name} switfly dodges.")
                                return
                    elif self.spell_list[spell_select] == "Charm":
                        print(f"The sorcerer attempts to soften the {enemy.name}'s demeanor!")
                        wis_save = enemy.wis + random.randint(1,20) - self.spell_power
                        print(f"The {enemy.name} rolls a {wis_save}")
                        self.spells -= 1 
                        if wis_save > 12:
                            print (f"The {enemy.name} shrugs it off!")
                            time.sleep(1.5)
                            return
                        else:
                            print(f"The {enemy.name} seems to hesitate!")
                            time.sleep(1.5)
                            enemy.proficency -= 2
                            return
                    elif self.spell_list[spell_select] == "Mage Armor":
                        if self.maxac == self.ac:
                            print("This spell can only take effect once!")
                        else:
                            print("You envelop yourself in a mystic shell!")
                            self.ac + 4
                            self.spells -= 1
                            return
                    elif self.spell_list[spell_select] == "Shield":
                            print("This spell is a reaction.")
                    else:
                        print("Invalid input.")
                else:
                    print("Invalid input.")

    def receive_damage(self, points, attack_roll):
        if self.ac + 4 >= attack_roll  and self.spells > 0: 
            while True:
                print(attack_roll)
                dodge_choice = input("Would you like to use a spell slot to dodge this attack? [y/n] ")
                if dodge_choice == "y":
                    print("A magic shield absorbs the blow!")
                    self.spells -= 1
                    if self.spells == 1:
                        print("You have one spell left!")
                    else:
                        print(f"You have {self.spells} spells left!")
                    break
                elif dodge_choice == "n":
                    print("%s received %d damage." % (self.name, points))
                    self.hp -= points
                    time.sleep(1.5)
                    if self.hp <= 0:
                        print("%s is dead." % self.name)
                    break
        else:
            print("%s received %d damage." % (self.name, points))
            self.hp -= points
            time.sleep(1.5)
            if self.hp <= 0:
                print("The sorcerer bravely faces the end and fades into light")



class Goblin(Character):
    on_fire = False
    def __init__(self):
        self.name = 'Goblin'
        self.max_hp = 8
        self.hp = 8
        self.minpower = 1
        self.power = 6
        self.coins = 4
        self.strength = 10
        self.dex = 1
        self.con = 14
        self.intel = 8
        self.wis = 8
        self.cha = 8
        self.dam_mod = 1
        self.ac = 13
        self.proficency = 2
        self.art = art_assets[self.name]
        self.intro = "The goblin's cruel face curls into a grin as he brandishes a bow at the"
        self.death_quote = "The goblin's shocked countanance becomes a grim mask of death as he is struck down."

    def attack(self, hero):
        if self.on_fire == True:
            self.hp -= 1
            print(f"The {self.name} takes 1 damage from their burn!")
        if not self.alive():
            return
        print("Goblin attacks %s" % (hero.name))
        if self.hp < 4:
            print("Fury of the small!")
            attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
            print(f"The {self.name} rolls a {attack_roll}!")
            if attack_roll - self.dam_mod - self.proficency == 20:
                print("Wow! A critical hit!")
                hero.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod) + 2, attack_roll)
                print(f"You took 2 extra damage from the Goblin's furious strike!")
                time.sleep(1.5)
            elif attack_roll >= enemy.ac:
                hero.receive_damage(random.randint(1,6) + self.dam_mod + 2, attack_roll)
                print(f"You took 2 extra damage from the Goblin's furious strike!")
                time.sleep(1.5)
            else:
                print(f"{self.name.capitalize()} misses!")
                time.sleep(1.5)
        else:
            attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
            print(f"The {self.name} rolls a {attack_roll}!")
            if attack_roll - self.dam_mod - self.proficency == 20:
                print("Wow! A critical hit!")
                hero.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                time.sleep(1.5)
            elif attack_roll >= enemy.ac:
                hero.receive_damage(random.randint(1,6) + self.dam_mod, attack_roll)
                time.sleep(1.5)
                return attack_roll
            else:
                print(f"{self.name.capitalize()} misses!")
                time.sleep(1.5)


class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.max_hp = 35
        self.hp = 35
        self.minpower = 1
        self.power = 6
        self.coins = 6
        self.strength = 10
        self.dex = 1
        self.con = 14
        self.intel = 8
        self.wis = 8
        self.cha = 8
        self.dam_mod = 2
        self.ac = 8
        self.proficency = 2
        self.art = art_assets[self.name]
        self.intro = "A putrid smell wafts into the air as the Zombie shambles towards the"

    def receive_damage(self, points, attack_roll):
        self.hp -= points
        print("%s received %d damage." % (self.name, points))
        time.sleep(1.5)
        if self.hp <= 0:
            if self.on_fire == True:
                print("The %s is dead and fades into a pile of ashes." % self.name)
            elif self.hp < 5:
                print("The zombie falls apart from massive damage.")
            else:
                self.hp = 1
                print("The zombie falters, but then rises back to fight.")

    def attack(self, enemy):
        if self.on_fire == True:
            self.hp -= 2
            print("Flames engulf the Zombie, scorching away exposed skin!")
        if not self.alive():
            return
        print("%s attacks %s" % (self.name, enemy.name))
        attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
        print(f"The {self.name} rolls a {attack_roll}!")
        if attack_roll - self.dam_mod - self.proficency == 20:
            print("Wow! Critical hit!")
            hero.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
            con_save = hero.con + random.randint(1,20)
            if con_save < 12:
                hero.is_poisoned = True
                print(f"The {hero.name} feels a rush of poison!")
            time.sleep(1.5)
        elif attack_roll >= hero.ac:
            hero.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
            con_save = hero.con + random.randint(1,20)
            if con_save < 12:
                hero.is_poisoned = True
                print(f"The {hero.name} feels a rush of poison!")
            time.sleep(1.5)
        else:
            print(f"{self.name.capitalize()} misses!")
            time.sleep(1.5)

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.max_hp = 30
        self.hp = 30
        self.minpower = 1
        self.power = 8
        self.coins = 10
        self.strength = 10
        self.dex = 2
        self.con = 14
        self.intel = 8
        self.wis = 4
        self.cha = 8
        self.dam_mod = 1
        self.ac = 13
        self.proficency = 2
        self.turn_counter = 0
        self.spells = 4
        self.spell_power = 0
        self.art = art_assets[self.name]
        self.intro = "A crackle of magical energy fills the room as the Wizard sets his wizened eyes on the"
        self.death_quote = "The wizard sadly grins and slowly claps as he burst into a flurry of magical lights."

    def attack(self, enemy):
        if self.on_fire == True:
            self.hp -= 1
            print(f"The {self.name} takes 1 damage from their burn!")
        if self.turn_counter == 0:
            print("The wizard coats himself in a mystic force!")
            self.ac += 4
            self.turn_counter += 1
        else:
            if not self.alive():
                return
            which_attack = random.randint(1,4)
            if self.spells < 1:
                print("The wizard has run out of spells!")
                print("%s attacks %s with his staff!" % (self.name, enemy.name))
                attack_roll = random.randint(1,20) + self.dam_mod + self.proficency
                print(f"The {self.name} rolls a {attack_roll}!")
                if attack_roll - self.dam_mod - self.proficency == 20:
                    print("Wow! Critical hit!")
                    hero.receive_damage((random.randint(1, self.power)) + (random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                    return
                elif attack_roll >= enemy.ac:
                    hero.receive_damage((random.randint(1, self.power)) + (self.dam_mod), attack_roll)
                    time.sleep(1.5)
                    return attack_roll
                else:
                    print(f"{self.name.capitalize()} misses!")
                    time.sleep(1.5)
                    return
            if which_attack == 1:
                print("The wizard attempts to muddle your mind!")
                wis_save = hero.wis + random.randint(1,20) - self.spell_power
                print(f"The {hero.name} rolls a {wis_save}")
                self.spells -= 1 
                if wis_save > 12:
                    print (f"The {hero.name} shrugs it off!")
                    time.sleep(1.5)
                else:
                    print(f"The {hero.name} is enveloped in a deep fog!")
                    time.sleep(1.5)
                    hero.proficency -= 2
            elif which_attack == 2 or which_attack == 3:
                print(f"The wizard sends a puddle of acid flying at the {hero.name}!")
                dex_save = hero.dex + random.randint(1,20) - self.spell_power
                self.spells -= 1
                print(f"The {hero.name} rolls a {dex_save}")
                if dex_save > 14:
                    print(f"The {hero.name} swiftly dodges!")
                elif dex_save > 12 and dex_save < 15:
                    damage_roll = random.randint(1,4) + self.spell_power
                    print(f"The {hero.name} barely jumps out of the way! Some acid splashes on him causing {damage_roll} damage!")
                    con_save = hero.con + random.randint(1,20)
                    if con_save < 12:
                        hero.is_poisoned = True
                        print(f"The {hero.name} feels a rush of poison!")
                    hero.hp -= damage_roll
                    time.sleep(1.5)
                elif dex_save <= 12:
                    damage_roll = random.randint(1,4) + random.randint(1,4) + self.spell_power
                    print(f"The {hero.name} is covered in acid, causing {damage_roll} damage!")
                    hero.hp -= damage_roll
                    con_save = hero.con + random.randint(1,20)
                    if con_save < 12:
                        hero.is_poisoned = True
                        print(f"The {hero.name} feels a rush of poison!")
                    time.sleep(1.5)
            else:
                print("The wizard mutters a dark incatation, increasing his power!")
                self.spell_power += 1
                time.sleep(1.5)


class Battle(object):
    def do_battle(self, hero, enemy):
        line_length = len(f"{enemy.intro} {hero.name}!" ) 
        print(line_length)
        print("=" * line_length)
        print(f"{enemy.intro} {hero.name}!")
        print("=" * line_length)
        print(enemy.art, hero.art)
        time.sleep(1.5)
        while hero.alive() and enemy.alive():
            hero.print_status()
            enemy.print_status()
            time.sleep(1.5)
            print("-----------------------")
            print("What do you want to do?")
            print("1. fight %s" % enemy.name)
            print("2. do nothing")
            print("3. throw torch")
            print("4. flee")
            print("> ",)
            user_input = input()
            if user_input == "1":
                enemy_init = random.randint(1,20) + enemy.dex
                hero_init = random.randint(1,20) + hero.dex
                if enemy_init > hero_init:
                    print(f"The {enemy.name} goes first!")
                    time.sleep(1.5)
                    enemy.attack(hero)
                    hero.attack(enemy)
                else:
                    print(f"The {hero.name} goes first!")
                    time.sleep(1.5)
                    hero.attack(enemy)
                    enemy.attack(hero)
            elif user_input == "2":
                enemy.attack(hero)
            elif user_input == "3":
                hero.throw_torch(enemy)
            elif user_input == "4":
                print("You leave with your life, if not your honor.")
                print("YOU LOSE")
                exit(0)
            else:
                print("Invalid input %r" % user_input)
                continue
        if hero.alive():
            print(f"You defeated the {enemy.name}!\nYou have {hero.hp} health left!")
            print(f"You find {enemy.coins} coins!")
            hero.coins += enemy.coins
            if hero.proficency < 2:
                hero.proficency = 2
                print("Your vision returns to normal")
            return True
        else:
            print("YOU LOSE!")
            return False

class Tonic(object):
    cost = 5
    name = 'Potion'
    def apply(self, hero):
        if hero.coins < 5:
            print("You can't afford this item!")
            return
        if hero.hp >= hero.max_hp:
            print("The potion will have no effect!")
        else:
            hero.hp += random.randint(1,8)
            if hero.hp > hero.max_hp:
                hero.hp = hero.max_hp
            print("%s's hp increased to %d." % (hero.name, hero.hp))
            hero.coins -= 5
            return hero.coins

class MoonGrass(object):
    cost = 5
    name = 'Moon Grass'
    def apply(self, hero):
        if hero.coins < 5:
            print("You can't afford this item!")
            return
        if hero.can_cast == False:
            print("This grass will have no effect!")
            return
        if hero.spells >= hero.max_spells:
            print("The grass will have no effect!")
        else:
            hero.spells += 1
            print("The %s's spells are increased to %d." % (hero.name, hero.spells))
            hero.coins -= 5
            return hero.coins

class Antidote(object):
    cost = 2
    name = 'Antidote'
    def apply(self, hero):
        if hero.coins < 2:
            print("You can't afford this item!")
            return
        if hero.is_poisoned == False:
            print("Luckily, you're not poisoned.")
            return
        else:
            hero.is_poisoned = False
            print("Rejoice! The %s is expunged of poison!" % (hero.name))
            hero.coins -= 2
            return hero.coins

class Wand(object):
    cost = 10
    name = 'Magic Wand'
    def apply(self, hero):
        if hero.coins < 10:
            print("You can't afford this item!")
            return
        if hero.can_cast == False:
            print("You can't use wands!")
            return
        if hero.has_wand == True:
            print("You already have a magic wand!")
        else:
            hero.spell_power += 1
            hero.has_wand = True
            print("The %s's spell damage is increased by one and they're harder to resist!" % (hero.name))
            hero.coins -= 10
            return hero.coins, hero.has_wand

class Sword(object):
    cost = 10
    name = 'Magic Weapon'
    def apply(self, hero):
        if hero.coins < 10:
            print("You can't afford this item!")
            return
        if hero.has_magic_weapon == True:
            print("You already have a magic weapon!")
        else:
            hero.dam_mod += 1
            hero.has_magic_weapon = True
            print("%s's attacks and damage are increased by one!" % (hero.name))
            hero.coins -= 10
            return hero.coins, hero.has_magic_weapon

class Shield(object):
    cost = 10
    name = 'Shield'
    def apply(self, hero):
        if hero.coins < 10:
            print("You can't afford this item!")
            return
        if hero.has_shield == True:
            print("You already have a magic weapon!")
        else:
            hero.ac += 2
            hero.has_shield = True
            print("%s's dodge rate is increased by 2!" % (hero.name))
            hero.coins -= 10
            return hero.coins, hero.has_shield

class Torch(object):
    cost = 2
    name = 'Torch'
    def apply(self, hero):
        if hero.coins < 2:
            print("You can't afford this item!")
            return
        if hero.has_torch == True:
            print("You already have a torch!")
        else:
            hero.has_torch = True
            print("The %s has a torch again!" % (hero.name))
            hero.coins -= 2
            return hero.coins, hero.has_torch

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, MoonGrass, Torch, Sword, Shield, Torch]
    def do_shopping(self, hero):
        print(art_assets["store"])
        print("==========================")
        print("Welcome to Markov's store!")
        print("==========================")
        while True:
            print("You have %d coins." % hero.coins)
            print("What do you want to do?")
            for i in range(len(Store.items)):
                item = Store.items[i]
                print("%d. buy %s (%d)" % (i + 1, item.name, item.cost))
            print("x. leave")
            user_input = input("> ")
            if user_input == "x":
                break
            else:
                ItemToBuy = Store.items[int(user_input) - 1]
                item = ItemToBuy()
                item.apply(hero)
                print("")
        print("See you later!")
        time.sleep(1.5)

#List of playable characters. As this is updated, make sure it matches the order of the dictionary
cast_list = ["Fighter", "Rogue", "Sorcerer"]
cast_dict = {"1": Fighter(), "2": Rogue(), "3": Sorcerer()}

def character_selector():
    while True:
        try:
            print("Who would you like to play as?  ")
            counter = 0
            for cast in cast_list:
                counter += 1 
                print(f"{counter}. {cast}")
            hero = cast_dict[input("> ")]
            if hero.is_playable:
                return hero
            else:
                raise NameError
        except:
            print("That is not a valid character!")

hero = character_selector()
enemies = [Goblin(), Zombie(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()
fight_list = 0
for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        
        exit(0)
    time.sleep(1.5)
    fight_list += 1
    if fight_list == len(enemies):
        break
    shopping_engine.do_shopping(hero)

print("YOU WIN!")
