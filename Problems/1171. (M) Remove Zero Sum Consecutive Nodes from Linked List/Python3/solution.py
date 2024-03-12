class Solution:
  def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # prefix sums with dictionaries

    sentinel = ListNode(0, head)
    cur = sentinel
    prefix_sum = 0
    # hist[key] is index of last element of the prefix list that sums up to key
    hist = {}
    while cur is not None:
      prefix_sum += cur.val
      # check whether current prefix sum already exists
      if prefix_sum in hist:
        prev = hist[prefix_sum]
        cur = prev.next
        # re-traverse the section to be deleted, removing each node's prefix sum in hist
        p = prefix_sum + cur.val
        while p != prefix_sum:
          del hist[p]
          cur = cur.next
          p += cur.val
        # remove section from linked list
        prev.next = cur.next
      else:
        hist[prefix_sum] = cur
      cur = cur.next
    
    return sentinel.next

