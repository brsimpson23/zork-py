# Brian Simpson
# CSCI 101 - Section C
# Zork.py

Thank you for downloading a copy of Zork, The PY Edition!
This Python Program is based loosely on the Storyline of Zork I, and is intended to run and function exactly like the original -
the only difference being that this version is written with Python and can therefore be run and downloaded for free!

To get started:
1. Unzip/Extract the files within this folder to your computer
1. If you do not have the latest version of Python 3 installed, please install it from http://www.python.org/download
1. Open the file named "zork.py"
1. Have Fun!

**Note: This program is built to run on Python 3.**

For this EC assignment I completed Section A, Section B, and Section C.  All parts should be successfully completed.

The first major struggle I ran into was an error saying there was a difference between spaces and tabs in the spacing.  This was an error originating from the original file, so I had to go through, and for every line,
redo all spaces and make them tabs.  All though this wasn't difficult, it was annoying.

I was also confused by the input required for part A.  The input required by the lab appeared to make the files more complex rather than less complex, going against the basis for the lab.  
However, once I got to part C, the reason for this change was obvious.

For Part C, I surprisingly didn't have any issues other than basic program run syntax.  Once I wrote the items functions they fit will into the zork.py file.


Custom Room Notes:

The custom room is the clearing in which the ogre was initially discovered.  However, rather than just running away from the ogre, you now have options.

The options that produce an output include:
1. Kill Ogre - you are never given any items to kill the ogre and so instead the ogre eats you.
2. Befriend Ogre - If you do not have a fish in your inventory you cannot befriend the ogre and the ogre eats you.  In order to acquire a fish, you must say fish four times while at the lake.  
Additionally, the fishing rod is no longer at the pier, it has to be retrieved from the attic.
By befriending the ogre by giving it the fish, you get the key that opens the trunk at the end of the game. Automatically returns to previous room.
3. Escape/Go North - returns you to the previous room.


Other Customizations (and Summary):

1. Fishing rod moved to attic.
2. Must fish four times to catch a fish.
3. Must befriend ogre with fish to get the chest's key.
4. Must use the key to open the chest.
5. Ogre can now eat you with the wrong prompt.  Not as broad of a range of commands for death as the grue.
6. Can return to the white house after going southwest.  This is accomplished by a 'go northeast' command.
7. Ladder exists in maze entrance room.  This ladder can be used to get back to the surface.
8. The skeleton holds a note regarding information about the maze and that the key is not in the maze.
9. There are multiple items that do absolutely nothing in the game.  These are included to throw off the player.


Speed Run Victory:
The fastest way to beat the game is type the following steps in the following order:
1. go east
2. go west
4. go up stairs
5. pick up fishing rod
6. go down stairs
7. go east
8. go south
9. go north
10. use fishing rod
11. fish
12. fish
13. fish
14. fish
15. pick up fish
16. go south
17. go southwest
18. go east
19. go south
20. use fish
21. befriend ogre
22. pick up key
23. go north
24. descend grating
25. descend staircase
26. use key
27. unlock trunk
28. open trunk