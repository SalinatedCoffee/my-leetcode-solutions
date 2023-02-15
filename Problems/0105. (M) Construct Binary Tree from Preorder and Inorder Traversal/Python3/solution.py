class Solution:
  def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    # recursively build subtrees

    # generate mapping from node to index in inorder
    io_n2i = {}
    for i in range(len(inorder)):
      io_n2i[inorder[i]] = i

    def recurse(lo, hi):
      # get preorder pivot from caller
      nonlocal pivot

      # invalid range
      if lo > hi or pivot >= len(inorder):
        return None
      
      # init node from preorder pivot
      node = TreeNode(preorder[pivot])
      # get inorder index of current node
      p_ioidx = io_n2i[preorder[pivot]]
      # advance pivot
      pivot += 1
      # recurse on left and right subtrees
      node.left = recurse(lo, p_ioidx-1)
      node.right = recurse(p_ioidx+1, hi)
      return node
    
    # set initial preorder pivot
    pivot = 0
    return recurse(0, len(inorder)-1)

