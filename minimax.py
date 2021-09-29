class decisionTree:
  def __init__(self, _score, _childs, _name):
    self.childs = _childs
    self.score = _score
    self.name = _name

  def repr(self, lvl = 0):
        ret = "\t" * lvl + self.name + "(" + str(self.score) + ")" + "\n"
        for child in self.childs:
            ret += child.repr(lvl + 1)
        return (ret)

# player 1 is inspector, player 0 is fantom
# odd is inspector fantom fantom inspector
# even is fantom inspector inspector fantom

MAX_VALUE = 1000

# add alpha beta stuff

class miniMax:
  def __init__(self, _tree):
    alpha = -1
    beta = -1
    self.tree = _tree
    self.decision = [True, False, False, True]

  def decide(self):
    self.tree.score = self.alphabeta(self.tree)
    return (self.tree.score)

  def calculate(self, tree, i=0):
    if i < len(self.decision) - 1:
      for child in tree.childs:
        child.score = self.calculate(child, i + 1)
    if self.decision[i]:
      return (maximiser(tree))
    else:
      return (minimiser(tree))

  def standardMinimax(self, tree, i=0):
    if len(tree.childs) < 1:
      return (tree.score)
    if self.decision[i]:
      v = -1
      for child in tree.childs:
        child.score = self.standardMinimax(child, i + 1)
        v = max(v, child.score)
    else:
      v = MAX_VALUE
      for child in tree.childs:
        child.score = self.standardMinimax(child, i + 1)
        v = min(v, child.score)
    return (v)

  # if decision[i] == decision[i+1] inverser la recherche de coupure -> si on cherche une alpha normalement check une beta et vise versa
  def alphabeta(self, tree, i=0, a=-1, b=MAX_VALUE):
    if len(tree.childs) < 1:
      return (tree.score)
    if self.decision[i]:
      v = -1
      for child in tree.childs:
        child.score = self.alphabeta(child, i + 1, a, b)
        v = max(v, child.score)
        if v >= b:
          #print(str(v) + ' v>=b ' + str(b) + " COUPURE BETA: " + str(a) + ' ' + str(b) + ' ' + tree.name + '->' + child.name)
          child.name += 'b'
          return v
        a = max(a, v)
    else:
      v = MAX_VALUE
      for child in tree.childs:
        child.score = self.alphabeta(child, i + 1, a, b)
        v = min(v, child.score)
        if a >= v:
          #print(str(a) + ' a>=v ' + str(v) + " COUPURE ALPHA: " + str(a) + ' ' + str(b) + ' ' + tree.name + '->' + child.name)
          child.name += 'a'
          return v
        b = min(b, v)
    return (v)


def maximiser(tree):
  val = -1
  for child in tree.childs:
    val = (val, child.score)[child.score > val]
  return (val)

def minimiser(tree):
  val = MAX_VALUE
  for child in tree.childs:
    val = (val, child.score)[child.score < val]
  return (val)


leaf1 = decisionTree(1, [], 'leaf1')
leaf2 = decisionTree(2, [], 'leaf2')
leaf3 = decisionTree(3, [], 'leaf3')
leaf4 = decisionTree(1, [], 'leaf4')
leaf5 = decisionTree(4, [], 'leaf5')
leaf6 = decisionTree(6, [], 'leaf6')
leaf7 = decisionTree(0, [], 'leaf7')
leaf8 = decisionTree(6, [], 'leaf8')
leaf9 = decisionTree(2, [], 'leaf9')
leaf10 = decisionTree(1, [], 'leaf10')
leaf11 = decisionTree(4, [], 'leaf11')
leaf12 = decisionTree(5, [], 'leaf12')
leaf13 = decisionTree(5, [], 'leaf13')
leaf14 = decisionTree(5, [], 'leaf14')
leaf15 = decisionTree(5, [], 'leaf15')
leaf16 = decisionTree(5, [], 'leaf16')

M11 = decisionTree(-1, [leaf1, leaf2], 'M11')
M12 = decisionTree(-1, [leaf3, leaf4], 'M12')
M13 = decisionTree(-1, [leaf5, leaf6], 'M13')
M14 = decisionTree(-1, [leaf7, leaf8], 'M14')
M15 = decisionTree(-1, [leaf9, leaf10], 'M15')
M16 = decisionTree(-1, [leaf11, leaf12], 'M16')
M17 = decisionTree(-1, [leaf13, leaf14], 'M17')
M18 = decisionTree(-1, [leaf15, leaf16], 'M18')

m21 = decisionTree(-1, [M11, M16], 'm21')
m22 = decisionTree(-1, [M12, M13], 'm22')
m23 = decisionTree(-1, [M15, M14], 'm23')
m24 = decisionTree(-1, [M18, M17], 'm24')

m31 = decisionTree(-1, [m21], 'm31')
m32 = decisionTree(-1, [m22, m23], 'm32')

M0 = decisionTree(-1, [m31, m32], 'M0')
print(M0.repr())

mm = miniMax(M0)
print("Decision: " + str(mm.decide()))
print(mm.tree.repr())
