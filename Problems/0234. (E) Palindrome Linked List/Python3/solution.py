class Solution:
  def isPalindrome(self, head: Optional[ListNode]) -> bool:
    # list reversal using deque
    
    rev = deque()
    cur = head
    while cur:
      rev.appendleft(cur.val)
      cur = cur.next
    cur = head
    while cur:
      if cur.val != rev.popleft():
        return False
      cur = cur.next

    return True

