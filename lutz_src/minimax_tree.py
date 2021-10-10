import copy
# define minimax tree class, to use with values

class Node:
    """
    Nodes for a tree with depth of 4, for all the choice within a single turn
    """
    def __init__(self, name, value):
        self.value = value
        self.name = name
        self.child = None

# generate tree path considering where characters are
def room0(isPink, names):
    move0 = Node("to 1", -1)
    move1 = Node("to 4", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room0 = [move0, move1]
    return room0

def room1(isPink, names):
    move0 = Node("to 0", -1)
    move1 = Node("to 2", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room1 = [move0, move1]
    if (isPink):
        move2 = Node("to 5", -1)
        move3 = Node("to 7", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
            move3.child = treeGen(names)
        room1.append([move2, move3])
    return room1

def room2(isPink, names):
    move0 = Node("to 1", -1)
    move1 = Node("to 3", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room2 = [move0, move1]
    if (isPink):
        move2 = Node("to 6", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
        room2.append(move2)
    return room2

def room3(isPink, names):
    move0 = Node("to 2", -1)
    move1 = Node("to 7", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room3 = [move0, move1]
    return room3

def room4(isPink, names):
    move0 = Node("to 0", -1)
    move1 = Node("to 5", -1)
    move2 = Node("to 8", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
        move2.child = treeGen(names)
    room4 = [move0, move1, move2]
    if (isPink):
        move3 = Node("to 9", -1)
        if (len(names) > 0):
            move3.child = treeGen(names)
        room4.append(move3)
    return room4

def room5(isPink, names):
    move0 = Node("to 4", -1)
    move1 = Node("to 6", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room5 = [move0, move1]
    if (isPink):
        move2 = Node("to 1", -1)
        move3 = Node("to 8", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
            move3.child = treeGen(names)
        room5.append([move2, move3])
    return room5

def room6(isPink, names):
    move0 = Node("to 5", -1)
    move1 = Node("to 7", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room6 = [move0, move1]
    if (isPink):
        move2 = Node("to 2", -1)
        move3 = Node("to 9", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
            move3.child = treeGen(names)
        room6.append([move2, move3])
    return room6

def room7(isPink, names):
    move0 = Node("to 3", -1)
    move1 = Node("to 6", -1)
    move2 = Node("to 9", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
        move2.child = treeGen(names)
    room7 = [move0, move1, move2]
    if (isPink):
        move3 = Node("to 1", -1)
        if (len(names) > 0):
            move3.child = treeGen(names)
        room7.append(move3)
    return room7

def room8(isPink, names):
    move0 = Node("to 4", -1)
    move1 = Node("to 9", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room8 = [move0, move1]
    if (isPink):
        move2 = Node("to 5", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
        room8.append(move2)
    return room8

def room9(isPink, names):
    move0 = Node("to 7", -1)
    move1 = Node("to 8", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = treeGen(names)
    room9 = [move0, move1]
    if (isPink):
        move2 = Node("to 4", -1)
        move3 = Node("to 6", -1)
        if (len(names) > 0):
            move2.child = treeGen(names)
            move3.child = treeGen(names)
        room9.append([move2, move3])
    return room9

rooms = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9]

# generate tree path for each characters
# todo: characters power
def pink(names, position):
    names[:] = [d for d in names if d.get('color') != "pink"]
    print(names)
    pink = Node("pink", -1)
    pink.child = rooms[position](True, names)
    return pink

def blue(names, position):
    names[:] = [d for d in names if d.get('color') != "blue"]
    blue = Node("blue", -1)
    blue.child = rooms[position](False, names)
    return blue

def red(names, position):
    names[:] = [d for d in names if d.get('color') != "red"]
    red = Node("red", -1)
    red.child = rooms[position](False, names)
    return red

def grey(names, position):
    names[:] = [d for d in names if d.get('color') != "grey"]
    grey = Node("grey", -1)
    grey.child = rooms[position](False, names)
    return grey

def black(names, position):
    names[:] = [d for d in names if d.get('color') != "black"]
    black = Node("black", -1)
    black.child = rooms[position](False, names)

def purple(names, position):
    names[:] = [d for d in names if d.get('color') != "purple"]
    purple = Node("purple", -1)
    purple.child = rooms[position](False, names)

def brown(names, position):
    names[:] = [d for d in names if d.get('color') != "brown"]
    brown = Node("brown", -1)
    brown.child = rooms[position](False, names)
    return brown

def white(names, position):
    names[:] = [d for d in names if d.get('color') != "white"]
    print(names)
    return rooms[position](False, names)

characters = {
    "pink": pink,
    "blue": blue,
    "red": red,
    "grey": grey,
    "black": black,
    "purple": purple,
    "brown": brown,
    "white": white
}

def treeGen(names):
    ## Format of input:
    # [
    #    {'color': 'brown', 'suspect': True, 'position': 9, 'power': False},
    #    {'color': 'red', 'suspect': True, 'position': 3, 'power': False},
    #    {'color': 'purple', 'suspect': True, 'position': 0, 'power': False},
    #    {'color': 'black', 'suspect': True, 'position': 1, 'power': False}
    # ]
    
    # root
    root = Node("Root", -1)
    root.child = []
    for n in names:
        # print (n)
        root.child.append(characters[n['color']](names, n['position']))
    return root
