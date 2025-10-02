class Solution:
  def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
    # simulation

    res = 0
    empty = 0
    while numBottles:
      # drink all available bottles
      res += numBottles
      empty += numBottles
      numBottles = 0
      # attempt to exchange empty bottles whenever possible
      if empty >= numExchange:
        empty -= numExchange
        numBottles += 1
        numExchange += 1

    return res

