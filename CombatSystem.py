import HumanClass
import random
import time

# Variable Randomizers

hp_randomizer = random.randint(250, 500)
bonus_attack_randomizer = random.randint(50, 85)
mana_randomizer = random.randint(300, 500)
potion_randomzier = random.randint(1, 3)

name_randomizer = random.randint(1, 5)
name = None
if name_randomizer == 1:
    name = "Rathal"
if name_randomizer == 2:
    name = "Iorath"
if name_randomizer == 3:
    name = "Bruh"
if name_randomizer == 4:
    name = "Lorimus"
if name_randomizer == 5:
    name = "Tramorin"

# Enemy Variables

Etotal_health = hp_randomizer + 100
Etotal_ba = bonus_attack_randomizer + 10
Etotal_mana = mana_randomizer + 50
Etotal_potions = potion_randomzier + 1

# Player Variables

Ptotal_health = hp_randomizer + 100
Ptotal_ba = bonus_attack_randomizer + 10
Ptotal_mana = mana_randomizer + 50
Ptotal_potions = potion_randomzier + 1



# Defining the Enemy and Player

Enemy = HumanClass.Wizard(name, Etotal_health, Etotal_ba,
                          Etotal_mana, Etotal_potions)

Player = HumanClass.Wizard("You", Ptotal_health, Ptotal_ba,
                           Ptotal_mana, Ptotal_potions)

# Combat System Loop

truevar = 1
while truevar == 1:

    main_input = input("\nPlease enter what you would like to do\nIf this your first time, please type in help: ")

    if main_input == "help":
        time.sleep(1)
        print("\nCommands:\n"
              "Attack - prompts you what spell you would like to cast and then attacks the enemy with that spell\n"
              "Heal - consumes a potion and heals you for 50 health\n"
              "Run - gives you a random chance to run away from the encounter\n"
              "Stats - checks your stats\n"
              "Enemy stats - checks your enemie's stats")

    elif main_input == "attack":
        time.sleep(0.25)
        attack_input = input("\nWould you like to summon tibbers, cast a fireball or basic attack: ")
        tibbers_tattack = 100 + bonus_attack_randomizer
        cf_attack = 50 + bonus_attack_randomizer
        normal_attack = 25 + bonus_attack_randomizer

        if attack_input == "summon tibbers":
            print("\nYou have attacked ", name, " for ", tibbers_tattack, " damage")
            Etotal_health -= tibbers_tattack

        elif attack_input == "cast fireball":
            print("You have attacked ", name, " for ", cf_attack, "damage")
            Etotal_health -= cf_attack

        elif attack_input == "basic attack":
            print("You have attacked ", name, " for ", normal_attack, "damage")
            Etotal_health -= normal_attack


        else:
            print("\nPlease enter a valid attack!")


            if Etotal_health <= 0:
                print("The enemy has died Hoorah!")
                break

        print("Your enemy's health is at", Etotal_health)

    elif main_input == "heal":
        time.sleep(0.25)
        if Ptotal_potions > 0:
            print("You have consumed a potion and have gained 50 health!")
            Ptotal_health += 50
            print("your new health is: ", Ptotal_health)

    elif main_input == "stats":
        time.sleep(0.25)
        print("\nYour health is at: ", Ptotal_health,
              "\nYour bonus attack is at: ", Ptotal_ba)

    elif main_input == "enemy stats":
        time.sleep(0.25)
        print("\nYour enemy's health is at: ", Etotal_health,
              "\nYour enemy's bonus attack is at: ", Etotal_ba)




    else:
        print("\nPlease enter a valid input!")

    AI_randomizer = random.randint(1, 4)
    time.sleep(5)
    print("\nIT IS NOW YOUR ENEMY'S TURN: ")
    if AI_randomizer == 1:
        time.sleep(0.5)
        print("\n", name, "has attacked you by summoning tibbers for ", 100 + Etotal_ba, " damage")
        Ptotal_health -= 100 + Etotal_ba

        if Ptotal_health <= 0:
            print("\n__________________\n"
                  "YOU HAVE BEEN DEFEATED")
            exit()

    if AI_randomizer == 2:
        time.sleep(0.5)
        print("\n", name, "has attacked you by casting fireball for ", 50 + Etotal_ba, " damage")
        Ptotal_health -= 50 + Etotal_ba

    if AI_randomizer == 3:
        time.sleep(0.5)
        if Etotal_potions > 0:
            print("\n", name, "has healed for 50 health by using a health potion!")
            Etotal_health += 50
        else:
            print("\n", name, "has checked his stats\nYour enemy's health is at: ", Etotal_health,
              "\nYour enemy's bonus attack is at: ", Etotal_ba)

    if AI_randomizer == 4:
        time.sleep(0.5)
        print("You enemy has skipped his turn!")

print("YOU HAVE BEAT THE ENEMY!!!!!")
