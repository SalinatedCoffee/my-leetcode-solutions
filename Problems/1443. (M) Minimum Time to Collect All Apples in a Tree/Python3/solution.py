class Solution:
  def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
    # DFS-based approach

    # if no edges return early
    if not edges:
      return 0

    # convert edge list to adjacency dictionary
    d_edges = {}
    for edge in edges:
      if edge[0] in d_edges:
        d_edges[edge[0]].append(edge[1])
      else:
        d_edges[edge[0]] = [edge[1]]
      if edge[1] in d_edges:
        d_edges[edge[1]].append(edge[0])
      else:
        d_edges[edge[1]] = [edge[0]]

    # number of all edges in valid path
    self.valid_edges = 0
    def helper(root, prev=None):
      # whether any neighbors are part of a valid path
      part_of_valid = False
      for i in d_edges[root]:
        # ignore caller
        if i == prev:
          continue
        res = helper(i, root)
        part_of_valid |= res
        # count edge between this and neighboring node if on valid path
        if res:
          # edges are traversed twice
          self.valid_edges += 2
      # return whether current node is part of valid path
      if hasApple[root]:
        return True
      return part_of_valid
    
    # start recursion
    helper(0)

    return self.valid_edges

