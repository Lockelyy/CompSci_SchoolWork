import time
import random

class Human:

    def __init__(self, name, hp, bonus_attack, mana, potions):
        """
        Represents a character in the monster game.

        @type name: string
        @type self: Human
        @type hp: float
        @type bonus_attack: float
        @type mana: float
        @type potions: float
        """
        self.hp = hp
        self.bonus_attack = bonus_attack
        self.mana = mana
        self.potions = potions
        self.name = name


    def receive_damage(self, damage):
        """
        Allows the selected character to take damage

        @type self: Human
        @type damage: int
        """
        self.hp -= damage

    def receive_health(self, health):
        """
        Allows the sele

        @type self: Human
        @type health: int
        """
        self.hp += health


    def normal_attack_player(self, character, normal_attack = 25):
        """
        Character is another humanoid class object.

        @type self: Human
        @type character: var?
        @type normal_attack: int
        """
        if self.mana >= normal_attack:
            print(self.name, " did a total damage of", normal_attack + self.bonus_attack)
            character.receive_damage(normal_attack + self.bonus_attack)

        else:
            print("You don't have enough mana to perform that action!")

    def check_stats(self):
        print(self.name, "stats")
        time.sleep(0.25)
        print("HP = ", self.hp)
        time.sleep(0.25)
        print("Bonus Attack = ", self.bonus_attack)

    def use_potion(self, character):
        if self.potions >= 1:
            print(self.name, " has used a potion and has gained ", 50, " health")
            character.receive_health(50)

        else:
            print("You dont have any potions left!")


class Wizard(Human):
    pass

    def cast_fireball(self, character, fireball_attack = 50):

        if self.mana >= fireball_attack:
            print(self.name, "casted fireball and did a total damage of", fireball_attack + self.bonus_attack)
            character.receive_damage(fireball_attack + self.bonus_attack)

        else:
            print(self.name, " doesn't have enough mana to perform that action!")

    def summon_tibbers(self, character, tibbers_attack = 100):

        if self.mana >= tibbers_attack:
            print(self.name, " summoned Tibbers and did a total damage of", tibbers_attack + self.bonus_attack)
            character.receive_damage(tibbers_attack + self.bonus_attack)

        else:
            print(self.name, " doesn't have enough mana to perform that action!")


class Assasin(Human):
    pass

    def hail_of_blades(self, character, hail_of_blades_attack = 100):

        if self.mana >= hail_of_blades_attack:
            print(self.name, " used hail of blades and did a total damage of", hail_of_blades_attack + self.bonus_attack)
            character.receive_damage(hail_of_blades_attack + self.bonus_attack)

        else:
            print(self.name, " doesn't have enough mana to perform that action!")

    def back_stab(self, character, back_stab_attack = 75):

        if self.mana >= back_stab_attack:
            print(self.name, " summoned Tibbers and did a total damage of", back_stab_attack + self.bonus_attack)
            character.receive_damage(back_stab_attack + self.bonus_attack)

        else:
            print(self.name, " doesn't have enough mana to perform that action!")


Billy = Wizard("Billy", 500, 50, 200, 1)
Jerome = Wizard("Jerome", 500, 50, 200, 1)
Billy.cast_fireball(Jerome)
Jerome.check_stats()
Jerome.use_potion(Jerome)
Jerome.check_stats()
