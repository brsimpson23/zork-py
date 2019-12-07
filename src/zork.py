import items

fish = 0
fishin = 0
caught = False

# Room 1
# North of House
def LakeRoom(north_house_inp):
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
                                print("---------------------------------------------------------")
                                print("You have not caught any fish.")
                else:
                        items.pick_up(item, room_num)

        elif 'put down' in north_house_inp.lower():
                item = (north_house_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in north_house_inp.lower():
                item = (north_house_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'fishing rod':
                                fishin = 1         
        
        elif north_house_inp.lower() == 'show inventory' or north_house_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif north_house_inp.lower() == ("go south"):
                room_num = 4
        elif north_house_inp.lower() == ("swim"):
                print("---------------------------------------------------------")
                print("You don't have a change of clothes and you aren't here on vacation.")
        elif north_house_inp.lower() == ("fish") or north_house_inp.lower() == ("go fishing"):
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
                        print("You need to use the fishing rod in order to fish.")
                        
        elif north_house_inp.lower() == ("kick the bucket"):
                alive = False

        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


lit = False
ladder = True

# Room 2
# Maze Entrance
def MazeEntrance(maze_inp):
        alive = True
        room_num = 2
        global lit
        global ladder

        if 'pick up' in maze_inp.lower():
                item = (maze_inp.lower())[8:]
                items.pick_up(item, room_num)
                if item == 'ladder':
                        ladder = False

        elif 'put down' in maze_inp.lower():
                item = (maze_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in maze_inp.lower():
                item = (maze_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'lantern':
                                lit = True
        
        elif maze_inp.lower() == 'show inventory' or maze_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif maze_inp.lower() == 'explore' or maze_inp.lower() == 'explore cavern':
                if not ladder:
                        print("---------------------------------------------------------")
                        print("You explore the cavern and find nothing.")
                else:
                        print("---------------------------------------------------------")
                        print("You explore the cavern and find a ladder hidden in the far corner.")

        elif maze_inp.lower() == ("go north"):
                room_num = 10
        elif maze_inp.lower() == ("go south"):
                room_num = 3
        elif maze_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


grue = False

# Room 3
# Maze Interior
def MazeInterior(maze_inp):
        alive = True
        room_num = 3
        global lit
        global grue

        if 'pick up' in maze_inp.lower():
                item = (maze_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in maze_inp.lower():
                item = (maze_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in maze_inp.lower():
                item = (maze_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'lantern':
                                lit = True
        
        elif maze_inp.lower() == 'show inventory' or maze_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif maze_inp.lower() == ("go north"):
                room_num = 2
        elif maze_inp.lower() == ("kick the bucket"):
                alive = False
        elif not grue:
                if not lit:
                        print("---------------------------------------------------------")
                        print("The Grue found you and ate you!")
                        alive = False
                else:
                        print("---------------------------------------------------------")
                        print("The Grue found you!")
                        print("You must run away to avoid being eaten!")
                        grue = True
        elif grue and maze_inp.lower() == ("run away"):
                room_num = 2
        else:
                print("---------------------------------------------------------")
                print("The Grue found you and ate you!")
                alive = False

        return [room_num, alive]


leaf = False
leaflet = True

# Room 4
# Front of House
def FrontOfHouse(second):
        global leaf
        global leaflet
        alive = True
        room_num = 4

        if 'pick up' in second.lower():
                item = (second.lower())[8:]
                if item == 'leaflet' and leaf:
                        leaflet = False
                        items.pick_up(item, room_num)
                elif item == 'leaflet' and not leaf:
                        print("---------------------------------------------------------")
                        print("Must open the mailbox to retrieve the leaflet.")
                else:
                        items.pick_up(item, room_num)

        elif 'put down' in second.lower():
                item = (second.lower())[9:]
                items.put_down(item, room_num)
                if item == 'leaflet':
                        leaflet = True

        elif 'use' in second.lower():
                item = (second.lower())[4:]
                items.useItem(item)
        
        elif second.lower() == 'show inventory' or second.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif second.lower() == ("take mailbox"):
                print("---------------------------------------------------------")
                print("It is securely anchored.")
        elif second.lower() == ("open mailbox"):
                if leaflet:
                        print("---------------------------------------------------------")
                        print("Opening the small mailbox reveals a leaflet.")
                else:
                        print("---------------------------------------------------------")
                        print("Mailbox is empty.")
                leaf = True
        elif second.lower() == ("go north"):
                room_num = 1
        elif second.lower() == ("go east"):
                room_num = 5
        elif second.lower() == ("open door"):
                print("---------------------------------------------------------")
                print("The door cannot be opened.")
        elif second.lower() == ("follow path"):
                print("---------------------------------------------------------")
                print("Go which direction?")
        elif second.lower() == ("take boards") or second.lower() == ("break boards"):
                print("---------------------------------------------------------")
                print("The boards are securely fastened.")
        elif second.lower() == ("look at house"):
                print("---------------------------------------------------------")
                print("The house is a beautiful colonial house which is painted white. It is clear that the owners must have been extremely wealthy.")
        elif second.lower() == ("go southwest"):
                room_num = 8
        elif second.lower() == ("read leaflet"):
                if not leaf:
                        print("---------------------------------------------------------")
                        print("Must open the mailbox to read the leaflet.")
                else:
                        if 'leaflet' in items.inventory:
                                print("---------------------------------------------------------")
                                print("Welcome to the Unofficial Python Version of Zork. Your mission is to find a Jade Statue.")
                        else:
                                print("---------------------------------------------------------")
                                print("You must pick up the leaflet to read the leaflet.")
        elif second.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 5
# Back of House
def BackOfHouse(back_inp):
        alive = True
        room_num = 5

        if 'pick up' in back_inp.lower():
                item = (back_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in back_inp.lower():
                item = (back_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in back_inp.lower():
                item = (back_inp.lower())[4:]
                items.useItem(item)
        
        elif back_inp.lower() == 'show inventory' or back_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif back_inp.lower() == ("go south") or back_inp.lower() == ("follow path"):
                room_num = 4
        elif back_inp.lower() == ("go west") or back_inp.lower() == ("enter house"):
                room_num = 6
                print("---------------------------------------------------------")
                print("Opening a rickety window you climb into the house.")
        elif back_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]
        

# Room 6
# Kitchen
def KitchenRoom(kitchen_inp):
        alive = True
        room_num = 6

        if 'pick up' in kitchen_inp.lower():
                item = (kitchen_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in kitchen_inp.lower():
                item = (kitchen_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in kitchen_inp.lower():
                item = (kitchen_inp.lower())[4:]
                items.useItem(item)
        
        elif kitchen_inp.lower() == 'show inventory' or kitchen_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif kitchen_inp.lower() == ("go up stairs") or kitchen_inp.lower() == ("go up"):
                room_num = 7
        elif kitchen_inp.lower() == ("go east") or kitchen_inp.lower() == ("exit house"):
                room_num = 5
        elif kitchen_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 7
# Attic
def AtticRoom(attic_inp):
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

        elif attic_inp.lower() == 'show inventory' or attic_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif attic_inp.lower() == ("go down stairs") or attic_inp.lower() == ("go down"):
                room_num = 6
        elif attic_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


# Room 8
# Southwest Loop
def ForestRoom(forest_inp):
        alive = True
        room_num = 8

        if 'pick up' in forest_inp.lower():
                item = (forest_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in forest_inp.lower():
                item = (forest_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in forest_inp.lower():
                item = (forest_inp.lower())[4:]
                items.useItem(item)
        
        elif forest_inp.lower() == 'show inventory' or forest_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif forest_inp.lower() == ("go west"):
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
def GratingRoom(grating_inp):
        alive = True
        room_num = 9
        global lit

        if 'pick up' in grating_inp.lower():
                item = (grating_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in grating_inp.lower():
                item = (grating_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in grating_inp.lower():
                item = (grating_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'lantern':
                                lit = True
        
        elif grating_inp.lower() == 'show inventory' or grating_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif grating_inp.lower() == ("go south"):
                room_num = 12
        elif grating_inp.lower() == ("go east"):
                room_num = 8
        elif grating_inp.lower() == ("descend grating") or grating_inp.lower() == ("go down") or grating_inp.lower() == ("go down grating"):
                room_num = 10
        elif grating_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]


height = False

# Room 10
# Grating Loop and Cave Input
def CaveRoom(cave_inp):
        alive = True
        room_num = 10
        global lit
        global height

        if 'pick up' in cave_inp.lower():
                item = (cave_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in cave_inp.lower():
                item = (cave_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in cave_inp.lower():
                item = (cave_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'lantern':
                                lit = True
                        if item == 'ladder':
                                height = True
        
        elif cave_inp.lower() == 'show inventory' or cave_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif cave_inp.lower() == ("go up") or cave_inp.lower() == ("ascend grating") or cave_inp.lower() == ("go up grating"):
                if height:
                        room_num = 9
                else:
                        print("---------------------------------------------------------")
                        print("You cannot jump high enough to escape.")
        elif cave_inp.lower() == ("descend staircase") or cave_inp.lower() == ("go down stairs"):
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


key = False
locked = True
statue = False

# Room 11
# End of game
def TrunkRoom(last_inp):
        alive = True
        room_num = 11
        global key
        global locked
        global lit
        global statue

        if 'pick up' in last_inp.lower():
                item = (last_inp.lower())[8:]
                items.pick_up(item, room_num)

        elif 'put down' in last_inp.lower():
                item = (last_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in last_inp.lower():
                item = (last_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'key':
                                key = True
                        if item == 'lantern':
                                lit = True
        
        elif last_inp.lower() == 'show inventory' or last_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif last_inp.lower() == ("go up stairs") or last_inp.lower() == ("go up"):
                room_num = 10

        elif last_inp.lower() == ("unlock trunk"):
                if key:
                        print("---------------------------------------------------------")
                        print("Trunk is now unlocked.")
                        locked = False
                else:
                        print("---------------------------------------------------------")
                        print("You need to use something to unlock the trunk")

        elif last_inp.lower() == ("open trunk"):
                if not locked:
                        print("---------------------------------------------------------")
                        print("You have found the Jade Statue and have completed your quest!")
                        statue = True
                else:
                        print("---------------------------------------------------------")
                        print("The trunk is still locked.")
                              
        elif last_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        if alive and statue:
                room_num = 'end'
        return[room_num, alive]


offering = False
ogre = True
                 
# Room 12
# Ogre Clearing
def OgreClearing(ogre_inp):
        alive = True
        room_num = 12
        global offering
        global ogre

        if 'pick up' in ogre_inp.lower():
                item = (ogre_inp.lower())[8:]
                if item == 'key':
                        if not ogre:
                                items.pick_up(item, room_num)
                        else:
                                print("You have not pacified the ogre.")
                else:
                        items.pick_up(item, room_num)

        elif 'put down' in ogre_inp.lower():
                item = (ogre_inp.lower())[9:]
                items.put_down(item, room_num)

        elif 'use' in ogre_inp.lower():
                item = (ogre_inp.lower())[4:]
                if items.useItem(item):
                        if item == 'fish':
                                offering = True
        
        elif ogre_inp.lower() == 'show inventory' or ogre_inp.lower() == 'inventory':
                print("---------------------------------------------------------")
                print(*items.inventory, sep = ', ')

        elif ogre_inp.lower() == ("go north"):
                room_num = 9
        elif ogre_inp.lower() == ("escape"):
                room_num = 9
        elif ogre_inp.lower() == ("kill ogre") or ogre_inp.lower() == ("fight ogre"):
                print("---------------------------------------------------------")
                print("You have nothing you can harm the ogre with.")
                print("The ogre ate you!")
                alive = False
        elif ogre_inp.lower() == ("steal key") or ogre_inp.lower() == ("take key"):
                print("---------------------------------------------------------")
                print("You have nothing you can harm the ogre with.")
                print("The ogre ate you!")
                alive = False
        elif ogre_inp.lower() == ("befriend ogre"):
                print("---------------------------------------------------------")
                if offering:
                        print("You befriended the ogre by giving the ogre the fish!")
                        print("In return the ogre gave you the key.")
                        (items.inventory).remove('fish')
                        ogre = False
                else:
                        print("---------------------------------------------------------")
                        print("You have nothing to befriend the ogre with.")
                        print("The ogre ate you!")
                        alive = False
        elif ogre_inp.lower() == ("kick the bucket"):
                alive = False
        else:
                print("---------------------------------------------------------")

        return [room_num, alive]

