class Solution:
  # naive solution, traverse list twice

  def __init__(self, head: Optional[ListNode]):
    self.length = 1
    self.head = head
    cur = head
    # determine length of list
    while cur.next:
      cur = cur.next
      self.length += 1

  def getRandom(self) -> int:
    # retrieve random nth node in list
    n = random.randrange(1, self.length+1)
    cur = self.head
    while n > 1 and cur.next:
      cur = cur.next
      n -= 1
    
    return cur.val

