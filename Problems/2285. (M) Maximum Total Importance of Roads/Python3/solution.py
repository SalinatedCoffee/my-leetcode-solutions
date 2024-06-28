class Solution:
  def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
    # greedy algorithm on sorted list
    
    # get degree of each node
    freq = [0] * n
    for u, v in roads:
      freq[u] += 1
      freq[v] += 1
    
    # sort list of degrees
    freq.sort()
    # greedily assign values and compute sum of importances
    ret = 0
    for i in range(n, 0, -1):
      ret += freq[i-1] * i

    return ret

