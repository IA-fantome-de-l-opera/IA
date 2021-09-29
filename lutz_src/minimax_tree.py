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

# class Choice():
#     def __init__(self, move, value):
#         self.move = move
#         self.value = value

def tree(names):
    # 4th layer
    leaf01 = Node(names[2], 0)
    leaf02 = Node(names[3], 0)
    leaf03 = Node(names[1], 0)
    leaf04 = Node(names[3], 0)
    leaf05 = Node(names[1], 0)
    leaf06 = Node(names[2], 0)
    leaf07 = Node(names[2], 0)
    leaf08 = Node(names[3], 0)
    leaf09 = Node(names[0], 0)
    leaf10 = Node(names[3], 0)
    leaf11 = Node(names[0], 0)
    leaf12 = Node(names[2], 0)
    leaf13 = Node(names[1], 0)
    leaf14 = Node(names[3], 0)
    leaf15 = Node(names[0], 0)
    leaf16 = Node(names[3], 0)
    leaf17 = Node(names[0], 0)
    leaf18 = Node(names[1], 0)
    leaf19 = Node(names[1], 0)
    leaf20 = Node(names[2], 0)
    leaf21 = Node(names[0], 0)
    leaf22 = Node(names[2], 0)
    leaf23 = Node(names[0], 0)
    leaf24 = Node(names[1], 0)

    # 3rd Layer
    branch3_01 = Node(names[1], 0)
    branch3_01.child = [leaf01, leaf02]
    
    branch3_02 = Node(names[2], 0)
    branch3_02.child = [leaf03, leaf04]
    
    branch3_03 = Node(names[3], 0)
    branch3_03.child = [leaf05, leaf06]
    
    branch3_04 = Node(names[0], 0)
    branch3_04.child = [leaf07, leaf08]
    
    branch3_05 = Node(names[2], 0)
    branch3_05.child = [leaf09, leaf10]
    
    branch3_06 = Node(names[3], 0)
    branch3_06.child = [leaf11, leaf12]
    
    branch3_07 = Node(names[0], 0)
    branch3_07.child = [leaf13, leaf14]
    
    branch3_08 = Node(names[1], 0)
    branch3_08.child = [leaf15, leaf16]
    
    branch3_09 = Node(names[3], 0)
    branch3_09.child = [leaf17, leaf18]
    
    branch3_10 = Node(names[0], 0)
    branch3_10.child = [leaf19, leaf20]
    
    branch3_11 = Node(names[1], 0)
    branch3_11.child = [leaf21, leaf22]
    
    branch3_12 = Node(names[2], 0)
    branch3_12.child = [leaf23, leaf24]

    # 2nd Layer
    branch2_1 = Node(names[0], 0)
    branch2_1.child = [branch3_01, branch3_02, branch3_03]

    branch2_2 = Node(names[1], 0)
    branch2_2.child = [branch3_04, branch3_05, branch3_06]
    
    branch2_3 = Node(names[2], 0)
    branch2_3.child = [branch3_07, branch3_08, branch3_09]

    branch2_4 = Node(names[3], 0)
    branch2_4.child = [branch3_10, branch3_11, branch3_12]

    # root
    root = Node(None, None)
    root.child = [branch2_1, branch2_2, branch2_3, branch2_4]

    print(root)
