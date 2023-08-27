class Solution:
  def findLongestChain(self, pairs: List[List[int]]) -> int:
    # greedy on sorted list
    
    n = len(pairs)
    pairs_sorted = sorted(pairs, key=lambda x: x[1])

    ret = 0
    prev = -1001
    for l, r in pairs_sorted:
      if l > prev:
        ret += 1
        prev = r

    return ret

