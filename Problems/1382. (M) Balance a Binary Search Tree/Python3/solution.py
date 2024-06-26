class Solution:
  def balanceBST(self, root: TreeNode) -> TreeNode:
    # inorder traversal

    # get list of nodes by traversing tree inorder
    nodes = []
    def lnr(node):
      if node is None:
        return
      lnr(node.left)
      nodes.append(node.val)
      lnr(node.right)
    
    # construct binary search tree using nodes in nodes[l:h+1]
    def reconstruct(l, h):
      if l > h:
        return None
      m = l + (h - l) // 2
      l = reconstruct(l, m-1)
      r = reconstruct(m+1, h)

      return TreeNode(nodes[m], l, r)

    lnr(root)

    return reconstruct(0, len(nodes)-1)

