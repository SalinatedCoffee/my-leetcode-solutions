class Solution:
  def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
    # Floyd-Warshall

    n = len(queries)
    # value of is_prereq[i][j] is True if i is prerequisite of j
    is_prereq = [[False] * numCourses for _ in range(numCourses)]
    for u, v in prerequisites:
      is_prereq[u][v] = True
    
    # use Floyd-Warshall to precompute is_prereq
    for i in range(numCourses):
      for s in range(numCourses):
        for t in range(numCourses):
          if is_prereq[s][i] and is_prereq[i][t]:
            is_prereq[s][t] = True
    
    # process queries using contents of is_prereq
    res = []
    for s, t in queries:
      res.append(is_prereq[s][t])

    return res

