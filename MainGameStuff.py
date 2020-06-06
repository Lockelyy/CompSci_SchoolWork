import MapClass
import HumanClass
import EventClass
import time
import random


GameMap = MapClass.LinkedList()
first_node = MapClass.Node("Hallway", "You have opened the door and have entered into a long hallway\n"
                                      "It seems to stretch out infinently and you can't even see the end\n"
                                      "Howver, you are able to see another door off to the side of the hall\n"
                                      "in the distance")
GameMap.head = first_node
second_node = MapClass.Node("Laboratory", "You cautiously walk down the hallway towards the door and slowly open it\n"
                                           "Suddenly you hear a loud voice blast SUBJECT MOVING TO SECTION 2 through\n"
                                           "Some sort of unseen intercom and then everything goes quiet again\n"
                                           "You open the door")
third_node = MapClass.Node("Strange Room", "")
fourth_node = MapClass.Node("Infinity Room", "\nLimping you enter into the next room and find yourself in a room\n"
                                             "That seems to go on forever, the walls are perfectly white and the door\n"
                                             "Behind you is now closed for some reason and there is a single button\n"
                                             "on the other side of the room")
fifth_node = MapClass.Node("Second Infinity Room", "\nAfter pressing the button you enter into the new room and its"
                                                   "exactly the same as the last room except that the walls are red\n"
                                                   "Suddenly a figure materializes in front of you and attacks")
sixth_node = MapClass.Node("Weird Room", "\nYou enter into the hidden compartment and crawl through a narrow vent\n"
                                         ", you emerge into a large room with racks and racks of what seems to be\n"
                                         "robot body parts and more cleaning robots. A large door sits at the back\n"
                                         "of the room and you eagerly think WOW another door!")
seventh_node = MapClass.Node("Final Room", "Sadly this door requires a passcode but the good news is some idiot left\n"
                                           "a note with the passcode on the keypad so you enter it and opens into a\n"
                                           "massive control room where dozens of scientists are sitting and\n"
                                           "observing camera feeds of the rooms you were previously in,suddenly it\n"
                                           "all comes back...this is an experiment and you are the subject\n"
                                           "you need to escape!")

first_node.next = second_node
second_node.next = third_node
third_node.next = fourth_node


def text_delay(text, delay):
    for i in text:
        time.sleep(delay)
        print(i, end='')
    print()


def movecheck_system(selected_node):
    cond1 = 1
    while cond1 == 1:
        main_inp = input("\nWhat would you like to do (Type in help for help): ")

        if main_inp == "next":
            print("you are now in", selected_node)
            break

        if main_inp == "help":
            print("\nType in *next* in order to proceed to the next tile\n"
                  "At each tile there is a random chance of an event happening")

        else:
            print("\nPlease enter a valid input!")


def eventinit(special_condition):

    if special_condition == "specialONE":
        print("\nBefore you can even react some sort of figure jumps on you and tackles you to the ground\n"
              "With your quick thinking however, your able to push him off")
        import CombatSystem
        time.sleep(1.5)
        print("\nAfter a lengthy fight you finally finish off the person while breathing heavily\n"
              "The person's eyes go dark and a red puddle pools around them\n"
              "Just as your about to proceed to the next room however, you see a coupl  e sparks fly from the body "
              "then dissapear\n"
              "You look around, wincing from the pain and see another door\nHow unique", 0.1)

    if special_condition == "specialTWO":
        import CombatSystem
        print("\nAfter this fight you can barely walk you are so tired, so you decide to rest. You crawl into a corner"
              "\nand lay there. All of a sudden a hidden compartment opens opposite from you and three small robots\n"
              "come out and take away the body of the person, dissapearing as quickly as they had emerged. Strange.\n"
              "You decide to explore the hidden compartment and try to open it. After a couple of minutes you suceed!")


    event_randomizer2 = random.randint(1, 3)

    if event_randomizer2 == 1:
        import CombatSystem

    if event_randomizer2 == 2:
        EventThing = EventClass.Event("Main Event")
        EventThing.item_event()

    if event_randomizer2 == 3:
        print("\nNo event occurs on this tile")


print("""
 _____ _            _   _
|_   _| |          | | | |
  | | | |__   ___  | |_| | ___  _   _ ___  ___
  | | | '_ \ / _ \ |  _  |/ _ \| | | / __|/ _ /
  | | | | | |  __/ | | | | (_) | |_| \__ \  __/
  \_/ |_| |_|\___| \_| |_/\___/ \__,_|___/\___|


""")

time.sleep(2)
text_delay("A Game By AV Incorporated™", 0.1)
time.sleep(0.25)
text_delay("\nYou wake up in a dark room and you can't seem to remember anything.\n"
           "You slowly get up and analyze your surroundings.\n"
           "All you see in the room is what seems to be a door giving off a faint glow in the distance\n"
           "Maybe it would be worth checking out?", 0.05)

# FIRST NODE SECTION
time.sleep(0.5)
print("\n")
movecheck_system(first_node)
time.sleep(1.25)
print("\n")
first_node.desc()
time.sleep(1)
print("\n")
eventinit("")

# SECOND NODE SECTION
time.sleep(0.5)
print("\n")
movecheck_system(second_node)
time.sleep(1.25)
print("\n")
second_node.desc()
time.sleep(1)
print("\n")
eventinit("")

#THIRD NODE SECTION
time.sleep(0.5)
print("\n")
movecheck_system(third_node)
time.sleep(1.25)
print("\n")
third_node.desc()
time.sleep(1)
print("\n")
eventinit("specialONE")

# FOURTH
time.sleep(0.5)
print("\n")
movecheck_system(fourth_node)
time.sleep(1.25)
print("\n")
fourth_node.desc()
time.sleep(1)
print("\n")
eventinit("")

# FIFTH
time.sleep(0.5)
print("\n")
movecheck_system(fifth_node)
time.sleep(1.25)
print("\n")
fifth_node.desc()
time.sleep(1)
print("\n")
eventinit("specialTWO")

# SIXTH
time.sleep(0.5)
print("\n")
movecheck_system(sixth_node)
time.sleep(1.25)
print("\n")
sixth_node.desc()
time.sleep(1)
print("\n")
eventinit("")

# SEVENTH
time.sleep(0.5)
print("\n")
movecheck_system(seventh_node)
time.sleep(1.25)
print("\n")
seventh_node.desc()
time.sleep(1)
print("\n")
eventinit("")

print("\nAfter fighting off the guards in the control room you see a red door marked with emergency escpae\n"
      "and you run out and emerge onto the roof of a building surrounded by even taller buildings\n"
      "you run towards an adajcent roof preparing to jump and then hit some sort of invisible wall\n"
      "your still in the experiment...suddenly everything goes black and then you wake up tied to a metal\n"
      "table with scientists surrounding, writing down notes in their clipnoards. You were an android the\n"
      "whole time and everyone you killed was too, this is all just a test to test Artifical Intelligece\n"
      "thats the last thing you realize as a voice says MEMORY WIPE SEQUENCE START and everything goes black")
print("\nTHANK YOU FOR PLAYING THE HOUSE BY ANDREY V!!!!!!!")





