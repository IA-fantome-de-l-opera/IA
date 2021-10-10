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
  def __init__(self, _tree, inspector):
    alpha = -1
    beta = -1
    self.tree = _tree
    if inspector:
      self.decision = [True, True, False, False, False, False, True, True]
    else:
      self.decision = [False, False, True, True, True, True, False, False]

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

  def alphabeta(self, tree, i=0, a=-1, b=MAX_VALUE):
    if len(tree.childs) < 1:
      return (tree.score)
    if self.decision[i]:
      v = -1
      for child in tree.childs:
        child.score = self.alphabeta(child, i + 1, a, b)
        v = max(v, child.score)
        if v >= b:
          child.name += 'b'
          return v
        a = max(a, v)
    else:
      v = MAX_VALUE
      for child in tree.childs:
        child.score = self.alphabeta(child, i + 1, a, b)
        v = min(v, child.score)
        if a >= v:
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
