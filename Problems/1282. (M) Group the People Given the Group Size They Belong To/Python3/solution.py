class Solution:
  def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
    # greedy

    n = len(groupSizes)
    ret = []
    groups = [[] for _ in range(n+1)]
    for i, g in enumerate(groupSizes):
      if len(groups[g]) == g:
        ret.append(groups[g])
        groups[g] = []
      groups[g].append(i)
    
    for i in range(1, n+1):
      if groups[i]:
        ret.append(groups[i])

    return ret

