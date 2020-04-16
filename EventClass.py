import random
import HumanClass

Jimmy = HumanClass.Wizard("Jimmy", 500, 150, 500, 2)


class Event:

    def __init__(self, name):

        """ Init method

        @type name: string


        :param name:
        """
        self.name = name



    def item_event(self):

        event_randomizer = random.randint(1, 5)

        if event_randomizer == 1:
            print("You have gotten a potion and have gained 50 health!")

        if event_randomizer == 2:
            damage_randomizer = random.randint(25, 150)
            print("You have recevied ", damage_randomizer, " damage from a hidden trap!")

        if event_randomizer == 3:
            mana_randomizer = random.randint(50, 100)
            print("You have found a mana well and have regained ", mana_randomizer, " mana")

        if event_randomizer == 4 or 5:
            print("You have gotten nothing")


#ASK ABOUT THE CLASS BUG THING, i dont know how to implement the methods from the Human Class into the Event class




Trap = Event("trap")
Trap.item_event()



