class Solution:
  def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # DFS-based approach

    # if no edges return early
    if not edges:
      return 0

    # convert edge list to adjacency list
    a_list = [[] for _ in range(n)]
    for u, v in edges:
      a_list[u].append(v)
      a_list[v].append(u)

    # total cost of valid path
    self.t_cost = 0
    def helper(root, prev=None):
      # whether any neighbors are part of a valid path
      part_of_valid = False
      for i in a_list[root]:
        # ignore caller
        if i == prev:
          continue
        res = helper(i, root)
        part_of_valid |= res
        # add cost between this and neighboring node if valid
        if res: 
          self.t_cost += 2
      # return whether current node is part of valid path
      if hasApple[root]:
        return True
      return part_of_valid
    
    # start recursion
    helper(0)

    return self.t_cost

