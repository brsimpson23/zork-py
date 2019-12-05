# Main game file

import zork



def PlayZork():
    print("---------------------------------------------------------")
    print("Welcome to Zork - The Unofficial Python Version.")
    
    leaf = 0
    alive = True
    returns = [4, True]

    while returns[1] == True:
        if returns[0] == 1:
            returns = zork.LakeRoom()
        
        elif returns[0] == 4:
            returns = zork.FrontOfHouse()

        elif returns[0] == 8:
            returns = zork.ForestRoom()

        elif returns[0] == 9:
            returns = zork.GratingRoom()

        elif returns[0] == 10:
            returns = zork.CaveRoom()

        elif returns[0] == 11:
            returns = zork.TrunkRoom()

    if not returns[1]:
        Death()

        #else:
            #user_inp = input("What do you do? ")
            


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
