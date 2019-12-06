# Items that exist in each room and the functions you can use to interact with them

#TODO Define items in each room
room1items = ['fish']
room2items = []
room3items = []
room4items = []
room5items = []
room6items = ['lantern']
room7items = ['fishing rod']
room8items = []
room9items = []
room10items = []
room11items = []
room12items = ['key']

allItems = [[], room1items, room2items, room3items, room4items, room5items, room6items, room7items, room8items, room9items, room10items, room11items, room12items]
inventory = []

# Returns item to be added to inventory if it exists in this room and removes it from the list of items in the room
def pick_up(itemName, roomNum):
    if itemName in allItems[roomNum]:
        allItems[roomNum].remove(itemName)
        inventory.append(itemName)
        print("Picked up", itemName)
        return itemName
    else:
        print("Not a valid item to pick up")
        return -1

# Puts the item down in the current room, adds it to the item list of the current room, 
# and returns 0 to indicate that it was successfully removed.
def put_down(itemName, roomNum):
    if itemName in inventory:
        print("You put down the", itemName)
        allItems[roomNum].append(itemName)
        inventory.remove(itemName)
        return 0
    else:
        print(itemName, 'not in inventory')
    return 0

# def useItem()
def useItem(itemName):
    if itemName in inventory:
        print("Using", itemName)
        return True
    else:
        print(itemName, "not in inventory")
        return False
