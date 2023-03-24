class Solution():
  def buildTree(self, inorder, postorder):
    # recursively build subtrees
  
    # base case
    if not inorder:
      return None
    
    # last element of postorder list is root
    root_val = postorder.pop()
    root = TreeNode(root_val)
    
    # find  position of the root in inorder list
    inorder_index = inorder.index(root_val)
    
    # recurse on left and right subtrees
    root.right = self.buildTree(inorder[inorder_index+1:], postorder)
    root.left = self.buildTree(inorder[:inorder_index], postorder)
    
    return root

