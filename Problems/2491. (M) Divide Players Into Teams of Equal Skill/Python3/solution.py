class Solution:
  def dividePlayers(self, skill: List[int]) -> int:
    # greedy algorithm on sorted list
    
    n = len(skill)
    skill.sort()
    # sum of first and last element in sorted list should be target skill
    l, h, tgt = 0, n-1, skill[0] + skill[-1]
    res = 0
    while l < h:
      if skill[l] + skill[h] != tgt:
        return -1
      res += skill[l] * skill[h]
      l += 1
      h -= 1

    return res

