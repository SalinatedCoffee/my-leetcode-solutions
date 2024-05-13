class Solution:
  def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # keep reference to nodes in list

    # traverse list and store reference to each node in list
    nodes = []
    cur = head
    while cur:
      nodes.append(cur)
      cur = cur.next
    # iterate on list in reverse while doubling each digit
    carry = 0
    for i in range(len(nodes)-1, -1, -1):
      val = nodes[i].val * 2 + carry
      carry = val // 10
      nodes[i].val = val % 10
    # if carry is not 0, create new node and make it the head
    if carry:
      head = ListNode(carry, head)
    
    return head

