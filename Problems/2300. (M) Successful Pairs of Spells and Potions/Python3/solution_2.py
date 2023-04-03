class Solution:
  def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
    # two pointers

    # sort spells while preserving original indices
    s_spells = [(e, i) for i, e in enumerate(spells)]
    s_spells.sort()
    potions.sort()

    pot_bound = len(potions) - 1
    ret = [0] * len(s_spells)
    for i in range(len(s_spells)):
      while pot_bound >= 0 and s_spells[i][0] * potions[pot_bound] >= success:
        pot_bound -= 1
      # store number of pairs in correct position
      ret[s_spells[i][1]] = len(potions) - pot_bound - 1
    
    return ret

