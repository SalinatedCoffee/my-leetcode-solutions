class Solution:
  def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
    # two pointers, reuse nodes

    # orig_cur is current node of original linked list
    # new_cur is tail of modified linked list
    orig_cur, new_cur = head.next, ListNode(-1, head)
    cur_sum = 0
    while orig_cur:
      if orig_cur.val == 0:
        new_cur = new_cur.next
        new_cur.val = cur_sum
        cur_sum = 0
      else:
        cur_sum += orig_cur.val
      orig_cur = orig_cur.next
    # properly terminate modified linked list
    new_cur.next = None

    return head

