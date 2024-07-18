class Solution:
  def countPairs(self, root: TreeNode, distance: int) -> int:
    # recursive DFS

    self.ret = 0

    def recurse(node):
      # return list of distances from node to each leaf node in its subtree

      # base case
      if node.left is None and node.right is None:
        return [1]

      l, r = [], []
      if node.left:
        l = recurse(node.left)
      if node.right:
        r = recurse(node.right)
      for l_d in l:
        for r_d in r:
          if l_d + r_d <= distance:
            self.ret += 1
      
      # update distances
      ret = l + r
      for i in range(len(ret)):
        ret[i] += 1

      return ret
    
    recurse(root)

    return self.ret

