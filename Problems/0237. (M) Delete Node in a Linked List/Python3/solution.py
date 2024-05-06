class Solution:
  def deleteNode(self, node: ListNode):

    node_next = node.next
    node.val = node_next.val
    node.next = node_next.next
    node_next.next = None

