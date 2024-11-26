class Solution:
  def findChampion(self, n: int, edges: List[List[int]]) -> int:
    # dictionary

    # determine indegree for each team
    indegrees = Counter([v for _, v in edges])
    # remove teams with non-zero indegree
    res = list(filter(lambda x: x[1] == 0, [(i, indegrees[i]) for i in range(n)]))

    # only return champion if there was exactly one result
    return res[0][0] if len(res) == 1 else -1

