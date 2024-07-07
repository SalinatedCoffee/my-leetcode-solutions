class Solution:
  def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
    # simulation
    
    ret = 0
    empty, full = 0, numBottles
    while full + empty >= numExchange:
      # drink full bottles
      ret += full
      # recompute number of each bottle
      full, empty = 0, full + empty
      full, empty = empty // numExchange, empty % numExchange

    return ret + full

