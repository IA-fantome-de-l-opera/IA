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

    def __repr__(self):
        st = "%s, " % (self.name)
        if self.child != None:
            for s in self.child:
                st += str(s)
            st += "\n"
        return st

# generate tree path considering where characters are
def room0(isPink, names):
    move0 = Node("to 1", -1)
    move1 = Node("to 4", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room0.child = [move0, move1]
    return room0

def room1(isPink, names):
    move0 = Node("to 0", -1)
    move1 = Node("to 2", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room1 = Node(None, -1)
    room1.child = [move0, move1]
    if (isPink):
        move2 = Node("to 5", -1)
        move3 = Node("to 7", -1)
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
            move3.child = copy.deepcopy(move0.child)
        room1.child.append([move2, move3])
    return room1

def room2(isPink, names):
    move0 = Node("to 1", -1)
    move1 = Node("to 3", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room2 = Node(None, -1)
    room2.child = [move0, move1]
    if (isPink):
        move2 = Node("to 6", -1)
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
        room1.child.append(move2)
    return room2

def room3(isPink, names):
    move0 = Node("to 2", -1)
    move1 = Node("to 7", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room3 = Node(None, -1)
    room3.child = [move0, move1]
    return room3

def room4(isPink, names):
    move0 = Node("to 0", -1)
    move1 = Node("to 5", -1)
    move2 = Node("to 8", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
        move2.child = copy.deepcopy(move0.child)
    room4 = Node(None, -1)
    room4.child = [move0, move1, move2]
    if (isPink):
        move3 = Node("to 9", -1)
        if (len(names) > 0):
            move3.child = copy.deepcopy(move0.child)
        room4.child.append(move3)
    return room4

def room5(isPink, names):
    move0 = Node("to 4", -1)
    move1 = Node("to 6", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room5 = Node(None, -1)
    room5.child = [move0, move1]
    if (isPink):
        move2 = Node("to 1", -1)
        move3 = Node("to 8")
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
            move3.child = copy.deepcopy(move0.child)
        room5.child.append([move2, move3])
    return room5

def room6(isPink, names):
    move0 = Node("to 5", -1)
    move1 = Node("to 7", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room6 = Node(None, -1)
    room6.child = [move0, move1]
    if (isPink):
        move2 = Node("to 2", -1)
        move3 = Node("to 9", -1)
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
            move3.child = copy.deepcopy(move0.child)
        room6.child.append([move2, move3])
    return room6

def room7(isPink, names):
    move0 = Node("to 3", -1)
    move1 = Node("to 6", -1)
    move2 = Node("to 9", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
        move2.child = copy.deepcopy(move0.child)
    room7 = Node(None, -1)
    room7.child = [move0, move1, move2]
    if (isPink):
        move3 = Node("to 1", -1)
        if (len(names) > 0):
            move3.child = copy.deepcopy(move0.child)
        room7.child.append(move3)
    return room7

def room8(isPink, names):
    move0 = Node("to 4", -1)
    move1 = Node("to 9", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room8 = Node(None, -1)
    room8.child = [move0, move1]
    if (isPink):
        move2 = Node("to 5", -1)
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
        room8.child.append(move2)
    return room8

def room9(isPink, names):
    move0 = Node("to 7", -1)
    move1 = Node("to 8", -1)
    if (len(names) > 0):
        move0.child = treeGen(names)
        move1.child = copy.deepcopy(move0.child)
    room9 = Node(None, -1)
    room9.child = [move0, move1]
    if (isPink):
        move2 = Node("to 4", -1)
        move3 = Node("to 6", -1)
        if (len(names) > 0):
            move2.child = copy.deepcopy(move0.child)
            move3.child = copy.deepcopy(move0.child)
        room9.child.append([move2, move3])
    return room9

rooms = [room0, room1, room2, room3, room4, room5, room6, room7, room8, room9]

# generate tree path for each characters
# todo: characters power
def pink(names, position):
    names[:] = [d for d in names if d.get('color') != "pink"]
    return rooms[position](True, names)

def blue(names, position):
    names[:] = [d for d in names if d.get('color') != "blue"]
    return rooms[position](False, names)

def red(names, position):
    names[:] = [d for d in names if d.get('color') != "red"]
    return rooms[position](False, names)

def grey(names, position):
    names[:] = [d for d in names if d.get('color') != "grey"]
    return rooms[position](False, names)

def black(names, position):
    names[:] = [d for d in names if d.get('color') != "black"]
    return rooms[position](False, names)

def purple(names, position):
    names[:] = [d for d in names if d.get('color') != "purple"]
    return rooms[position](False, names)

def brown(names, position):
    names[:] = [d for d in names if d.get('color') != "brown"]
    return rooms[position](False, names)

def white(names, position):
    names[:] = [d for d in names if d.get('color') != "white"]
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
    
    print(names)
    # root
    root = Node(None, None)
    root.child = []
    for n in names:
        # print (n)
        root.child.append(characters[n['color']](names, n['position']))
    return root
