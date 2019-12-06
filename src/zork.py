import items

leaf = 0

# Room 1
# North of House
def LakeRoom(north_house_inp, items):
        alive = True
        room_num = 1

        if north_house_inp.lower() == ("go south"):
                room_num = 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif north_house_inp.lower() == ("fish"):
                print("---------------------------------------------------------")
                print("You spend some time fishing but nothing seems to bite.")
        elif north_house_inp.lower() == ("kick the bucket"):
                alive = False

        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room = 4
def FrontOfHouse(second, items):
        global leaf
        alive = True
        room_num = 4

        if second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
        elif second.lower() == ("open mailbox"):
                print("---------------------------------------------------------")
                print("Opening the small mailbox reveals a leaflet.")
                leaf = 1
        elif second.lower() == ("go north"):
                room_num = 1
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif second.lower() == ("take boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif second.lower() == ("go southwest"):
                room_num = 8
        elif second.lower() == ("read leaflet"):
                if leaf == 0:
                        print("---------------------------------------------------------")
                        print("Must open the mailbox to read the leaflet.")
                elif leaf == 1:
                        print("---------------------------------------------------------")
                        print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
        elif second.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]
                

# Room 8
# Southwest Loop
def ForestRoom(forest_inp, items):
        alive = True
        room_num = 8

        if forest_inp.lower() == ("go west"):
                print("---------------------------------------------------------")
                print("You would need a machete to go further west.")
        elif forest_inp.lower() == ("go north"):
                print("---------------------------------------------------------")
                print("The forest becomes impenetrable to the North.")
        elif forest_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("Storm-tossed trees block your way.")
        elif forest_inp.lower() == ("go east"):
                room_num = 9
        elif forest_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 9
# East Loop and Grating Input
def GratingRoom(grating_inp, items):
        alive = True
        room_num = 9

        if grating_inp.lower() == ("go south"):
                print("---------------------------------------------------------")
                print("You see a large ogre and turn around.")
        elif grating_inp.lower() == ("descend grating"):
                room_num = 10
        elif grating_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 10
# Grating Loop and Cave Input
def CaveRoom(cave_inp, items):
        alive = True
        room_num = 10

        if cave_inp.lower() == ("descend staircase"):
                room_num = 11
        elif cave_inp.lower() == ("take skeleton"):
                print("---------------------------------------------------------")
                print("Why would you do that? Are you some sort of sicko?")
        elif cave_inp.lower() == ("smash skeleton"):
                print("---------------------------------------------------------")
                print("Sick person. Have some respect mate.")
        elif cave_inp.lower() == ("light up room"):
                print("---------------------------------------------------------")
                print("You would need a torch or lamp to do that.")
        elif cave_inp.lower() == ("break skeleton"):
                print("---------------------------------------------------------")
                print("I have two questions: Why and With What?")
        elif cave_inp.lower() == ("go down staircase"):
                room_num = 11
        elif cave_inp.lower() == ("scale staircase"):
                room_num = 11
        elif cave_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 11
# End of game
def TrunkRoom(last_inp, items):
        alive = True
        room_num = 11

        if last_inp.lower() == ("open trunk"):
                print("---------------------------------------------------------")
                print("You have found the Jade Statue and have completed your quest!")
        elif last.inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        if alive:
                # Exit loop at the end of game
                exit_inp = input("Do you want to continue? Y/N ")
                if exit_inp.lower() == ("n"):
                        exit()
                if exit_inp.lower() == ("y"):
                        Play_Zork()

                        
