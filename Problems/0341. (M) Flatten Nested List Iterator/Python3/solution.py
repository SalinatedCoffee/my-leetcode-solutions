class NestedIterator:
  # stacks
  def __init__(self, nestedList: [NestedInteger]):
    self._h = []
    self._h.extend(reversed(nestedList))
  
  def next(self) -> int:
    return self._h.pop().getInteger()
      
  def hasNext(self) -> bool:
    # if next element exists, pre-flatten it into self._h
    
    while self._h:
      c = self._h[-1]
      if c.isInteger():
        return True
      self._h.pop()
      self._h.extend(reversed(c.getList()))

    return False

