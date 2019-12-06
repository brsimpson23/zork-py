# Main game file

import zork
import items


def PlayZork():
    print("---------------------------------------------------------")
    print("Welcome to Zork - The Unofficial Python Version.")
    
    returns = [4, True]

    while returns[1] == True:
        if returns[0] == 1:
            print("---------------------------------------------------------")
            print("You find yourself at the edge of a beautiful lake aside rolling hills.")
            print("A small pier juts out into the lake.")
            print("(You can see a white house in the distance to the south.)")
            user_inp = input("What do you do? ")
            returns = zork.LakeRoom(user_inp, items.allItems)

        if returns[0] == 2:
            print("---------------------------------------------------------")
            print("You find yourself in a large cavern. ")
            print("There appears to be another path to the south.")
            print("The new path is even darker than the one you are currently on.")
            user_inp = input("What do you do? ")
            returns = zork.MazeEntrance(user_inp, items.allItems)

        if returns[0] == 3:
            print("---------------------------------------------------------")
            print("You have entered the maze.")
            print("There is no apparent way out and it is pitch black.")
            print("You feel as though there is something watching your every move.")
            user_inp = input("What do you do? ")
            returns = zork.MazeInterior(user_inp, items.allItems)
        
        elif returns[0] == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("You can see a small lake to the north.")
            print("To the east there is another path to the back of the house.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            user_inp = input("What do you do? ")
            returns = zork.FrontOfHouse(user_inp, items.allItems)
            
        elif returns[0] == 5:
            print("---------------------------------------------------------")
            print("You find yourself on the backside of the house.")
            print("There is a window slightly ajar to the west.")
            print("A path to the south leads somewhere mysterious.")
            user_inp = input("What do you do? ")
            returns = zork.BackOfHouse(user_inp, items.allItems)

        elif returns[0] == 6:
            print("---------------------------------------------------------")
            print("You find yourself in a dimly lit kitchen with dust covering the floor.")
            if "lantern" in allItems[6]:
                print("A lantern rests on the kitchen island.")
            print("A set of stairs go up to another room.")
            user_inp = input("What do you do? ")
            returns = zork.KitchenRoom(user_inp, items.allItems)

        elif returns[0] == 7:
            print("---------------------------------------------------------")
            print("You go up and find yourself in the attic.")
            if 'fishing rod' in items.allItems[7]:
                print("The attic appears to be bare except for dust and a fishing rod in the corner.")
            user_inp = input("What do you do? ")
            returns = zork.AtticRoom(user_inp, items.allItems)

        elif returns[0] == 8:
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions.")
            print("To the east, there appears to be sunlight.")
            user_inp = input("What do you do? ")
            returns = zork.ForestRoom(user_inp, items.allItems)

        elif returns[0] == 9:
            print("---------------------------------------------------------")
            print("You are in a clearing, with a forest surrounding you on all sides. A path leads south.")
            print("There is an open grating, descending into darkness.")
            user_inp = input("What do you do? ")
            returns = zork.GratingRoom(user_inp, items.allItems)

        elif returns[0] == 10:
            print("---------------------------------------------------------")
            print("You are in a tiny cave with a dark, forbidding staircase leading down.")
            print("To the south you also see a dark, winding path leading into the unknown.")
            print("There is a skeleton of a human male in one corner.")
            user_inp = input("What do you do? ")
            returns = zork.CaveRoom(user_inp, items.allItems)

        elif returns[0] == 11:
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            user_inp = input("What do you do? ")
            continued = zork.TrunkRoom(user_inp, items.allItems)

        elif returns[0] == 12:
            print("---------------------------------------------------------")
            print("You enter into a clearing a see a massive ogre sitting by a stream.")
            if ogre:
                print("You notice a key around the ogre's neck as it bends over to drink.")
                print("The ogre hasn't noticed you yet, leaving open the possibility to escape.")
            user_inp = input("What do you do? ")
            returns = zork.OgreClearing(user_inp, items.allItems)

    if not returns[1]:
        continued = Death()

    if continued == 1:
        PlayZork()
    

def Death():
    continued = 0
    print("---------------------------------------------------------")
    print("You die.")
    print("---------------------------------------------------------")
    dead_inp = input("Do you want to continue? Y/N ")
    if dead_inp.lower() == ("n"):
            exit()
    if dead_inp.lower() == ("y"):
            continued = 1
    return continued

PlayZork()

def PrintOutput(s):
    print("OUTPUT", s)
