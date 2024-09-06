class Solution:
  def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:

    delete = set(nums)
    sentinel = ListNode(-1, head)
    prev, cur = sentinel, head
    while cur:
      if cur.val in delete:
        prev.next = cur.next
        # technically not needed, but properly detach removed node from linked list
        temp = cur.next
        cur.next = None
        cur = temp
      else:
        prev, cur = cur, cur.next

    return sentinel.next

