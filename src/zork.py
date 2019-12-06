import items

leaf = 0
fish = 0
fishin = 0
caught = False

# Room 1
# North of House
def LakeRoom(north_house_inp, inventory):
        global fish
        global fishin
        global caught
        alive = True
        room_num = 1

        if 'pick up' in north_house_inp.lower():
                item = (north_house_inp.lower())[8:]
                if item == 'fish':
                        if caught:
                                items.pick_up(item, room_num)
                        else:
                                print("You have not caught any fish.")
                else:
                        items.pick_up(item, room_num)

        elif 'put down' in north_house_inp.lower():
                item = (north_house_inp.lower())[9:]
                items.put_down(item, room_num[1])

        elif 'use' in north_house_inp.lower():
                item = (north_house_inp.lower())[4:]
                if items.useItem(item) and item == 'fishing rod':
                        fishin = 1
        
        elif north_house_inp.lower() == 'show inventory' or north_house_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif north_house_inp.lower() == ("go south"):
                room_num = 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif north_house_inp.lower() == ("fish"):
                if fishin == 1:
                        if fish != 3:
                                print("---------------------------------------------------------")
                                print("You spend some time fishing but nothing seems to bite.")
                                fish += 1
                        elif fish == 3:
                                print("---------------------------------------------------------")
                                print("You finally caught a fish!")
                                fish += 1
                                caught = True
                else:
                        print("---------------------------------------------------------")
                        print("You are not fishing with anything.")
                        
        elif north_house_inp.lower() == ("kick the bucket"):
                alive = False

        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 2
# Maze Entrance
def MazeEntrance(maze_inp, inventory):
        alive = True
        room_num = 2

        if maze_inp.lower() == ("go north"):
                room_num = 10
        elif maze_inp.lower() == ("go south"):
                room_num = 3
        elif maze_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 3
# Maze Interior
def MazeInterior(maze_inp, inventory):
        alive = True
        room_num = 3

        if maze_inp.lower() == ("go north"):
                room_num = 2
        elif maze_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")
                print("The Grue found you and ate you!")
                alive = False

        return [room_num, alive]


# Room 4
# Front of House
def FrontOfHouse(second, inventory):
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
        elif second.lower() == ("go east"):
                room_num = 5
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


# Room 5
# Back of House
def BackOfHouse(back_inp, inventory):
        alive = True
        room_num = 5

        if back_inp.lower() == ("go south"):
                room_num = 4
        if back_inp.lower() == ("go west"):
                room_num = 6
                print("Opening a rickety window you climb into the house.")
        elif back_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]
        

# Room 6
# Kitchen
def KitchenRoom(kitchen_inp, inventory):
        alive = True
        room_num = 6

        if kitchen_inp.lower() == ("go up stairs"):
                room_num = 7
        elif kitchen_inp.lower() == ("go east"):
                room_num = 5
        elif kitchen_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 7
# Attic
def AtticRoom(attic_inp, inventory):
        alive = True
        room_num = 7

        if 'pick up' in attic_inp.lower():
            item = (attic_inp.lower())[8:]
            items.pick_up(item, room_num)

        elif 'put down' in attic_inp.lower():
            item = (attic_inp.lower())[9:]
            items.put_down(item, room_num)

        elif 'use' in attic_inp.lower():
            item = (attic_inp.lower())[4:]
            items.useItem(item)

        elif attic_inp.lower() == 'show inventory' or attic_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        if attic_inp.lower() == ("go down stairs"):
                room_num = 6
        elif attic_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 8
# Southwest Loop
def ForestRoom(forest_inp, inventory):
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
        elif forest_inp.lower() == ("go northeast"):
                room_num = 4
        elif forest_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 9
# East Loop and Grating Input
def GratingRoom(grating_inp, inventory):
        alive = True
        room_num = 9

        if grating_inp.lower() == ("go south"):
                room_num = 12
        elif grating_inp.lower() == ("descend grating"):
                room_num = 10
        elif grating_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 10
# Grating Loop and Cave Input
def CaveRoom(cave_inp, inventory):
        alive = True
        room_num = 10

        if cave_inp.lower() == ("descend staircase"):
                room_num = 11
        elif cave_inp.lower() == ("go south"):
                room_num = 2
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
def TrunkRoom(last_inp, inventory):
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
                continued = 0
                # Exit loop at the end of game
                exit_inp = input("Do you want to continue? Y/N ")
                if exit_inp.lower() == ("n"):
                        exit()
                if exit_inp.lower() == ("y"):
                        continued = 1
                return continued

                        
# Room 12
# Ogre Clearing
def OgreClearing(ogre_inp, inventory):
        alive = True
        room_num = 12

        if ogre_inp.lower() == ("go north"):
                room_num = 9
        elif ogre_inp.lower() == ("escape"):
                room_num = 9
        elif ogre_inp.lower() == ("kill ogre"):
                print("---------------------------------------------------------")
                print("You have nothing you can harm the ogre with.")
                print("The ogre ate you!")
                alive = False
        elif ogre_inp.lower() == ("befriend ogre"):
                print("---------------------------------------------------------")
                if fish in items:
                        print("You befriended the ogre by giving the ogre the fish!")
                        print("In return the ogre gave you the key.")
                        print("Key has been added to your inventory.")
                        room_num = 9
                else:
                        print("---------------------------------------------------------")
                        print("You have nothing to befriend the ogre with.")
                        print("The ogre ate you!")
        elif ogre_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]

