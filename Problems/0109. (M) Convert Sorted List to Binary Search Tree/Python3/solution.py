class Solution:
  # recursive solution with two pointers
  def sortedListToBST(self, head):
    # sanity checks
    if not head:
      return None
    if not head.next:
      return TreeNode(head.val)

    return self.recurse(head, None)
    
  def recurse(self, head, tail):
    if head is tail:
      return None
    slow = fast = head

    while fast is not tail and fast.next is not tail:
      slow = slow.next
      fast = fast.next.next
    
    # recursively construct subtrees
    left = self.recurse(head, slow)
    right = self.recurse(slow.next, tail)
    return TreeNode(slow.val, left, right)

