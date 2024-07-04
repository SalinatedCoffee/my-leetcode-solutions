class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # two pointers

    # orig_cur is current node of original linked list
    orig_cur, sentinel = head.next, ListNode(-1)
    # new_cur is tail of modified linked list
    new_cur = sentinel
    cur_sum = 0
    while orig_cur:
      if orig_cur.val == 0:
        new_cur.next = ListNode(cur_sum)
        new_cur, cur_sum = new_cur.next, 0
      else:
        cur_sum += orig_cur.val
      orig_cur = orig_cur.next

    return sentinel.next

