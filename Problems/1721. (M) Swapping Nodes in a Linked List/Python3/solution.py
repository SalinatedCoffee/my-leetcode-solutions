class Solution:
  def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # cast list to array and swap values

    nodes = []
    cur = head
    while cur:
      nodes.append(cur)
      cur = cur.next
    nodes[k-1].val, nodes[-k].val = nodes[-k].val, nodes[k-1].val

    return head

