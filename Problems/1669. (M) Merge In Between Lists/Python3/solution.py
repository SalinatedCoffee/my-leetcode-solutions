class Solution:
  def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
    # linear traversal of linked lists

    l1_start, l1_end = list1, list1
    l2_tail = list2
    # find a-1 th node
    while a > 1:
      l1_start = l1_start.next
      a -= 1
    # find b+1 th node
    while b >= 0:
      l1_end = l1_end.next
      b -= 1
    # find tail node of list2
    while l2_tail.next is not None:
      l2_tail = l2_tail.next

    l1_start.next = list2
    l2_tail.next = l1_end

    return list1 if a else list2

