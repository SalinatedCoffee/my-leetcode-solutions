class Solution:
  def findJudge(self, n: int, trust: List[List[int]]) -> int:
    # judge only has incoming edges
    # keep counter for everyone
    # increment for incoming edges, decrement for outgoing
    
    people = [0 for _ in range(n+1)]

    for u, v in trust:
      people[v] += 1
      people[u] -= 1
    
    for i in range(1, n+1):
      if people[i] == n-1:
        return i
    
    return -1

