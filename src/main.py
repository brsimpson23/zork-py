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
            print("A fishing rod rests on the pier.")
            print("(You can see a white house in the distance to the south.)")
            user_inp = input("What do you do? ")
            returns = zork.LakeRoom(user_inp, items.allItems)
        
        elif returns[0] == 4:
            print("---------------------------------------------------------")
            print("You are standing in an open field west of a white house, with a boarded front door.")
            print("You can see a small lake to the north.")
            print("(A secret path leads southwest into the forest.)")
            print("There is a Small Mailbox.")
            user_inp = input("What do you do? ")
            returns = zork.FrontOfHouse(user_inp, items.allItems)

        elif returns[0] == 8:
            print("---------------------------------------------------------")
            print("This is a forest, with trees in all directions. To the east, there appears to be sunlight.")
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
            print("There is a skeleton of a human male in one corner.")
            user_inp = input("What do you do? ")
            returns = zork.CaveRoom(user_inp, items.allItems)

        elif returns[0] == 11:
            print("---------------------------------------------------------")
            print("You have entered a mud-floored room.")
            print("Lying half buried in the mud is an old trunk, bulging with jewels.")
            user_inp = input("What do you do? ")
            returns = zork.TrunkRoom(user_inp, items.allItems)

    if not returns[1]:
        Death()


def Death():
        print("---------------------------------------------------------")
        print("You die.")
        print("---------------------------------------------------------")
        dead_inp = input("Do you want to continue? Y/N ")
        if dead_inp.lower() == ("n"):
                exit()
        if dead_inp.lower() == ("y"):
                Play_Zork()

PlayZork()

def PrintOutput(s):
    print("OUTPUT", s)
