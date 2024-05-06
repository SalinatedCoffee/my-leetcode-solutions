class Solution:
  def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # decreasing monotonic stack

    sentinel = ListNode(float('inf'), head)
    stack = [sentinel]
    cur = head
    while cur:
      # remove previously selected nodes with value smaller than current
      while stack and stack[-1].val < cur.val:
        stack.pop()
      stack.append(cur)
      cur = cur.next
    
    # 'reassemble' contents of stack into linked list
    m = len(stack)
    prev = stack[0]
    # Python stacks are just lists
    #   may need to link nodes in reverse order in other languages
    for i in range(1, m):
      prev.next = stack[i]
      prev = stack[i]

    return sentinel.next

