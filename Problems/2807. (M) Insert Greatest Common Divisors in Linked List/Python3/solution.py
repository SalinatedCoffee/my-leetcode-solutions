class Solution:
  def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:

    def gcd(a, b):
      while b:
        t = b
        b = a % b
        a = t
      return a

    prev, cur = head, head.next
    while cur:
      gcd_node = ListNode(gcd(prev.val, cur.val), cur)
      prev.next = gcd_node
      prev = cur
      cur = cur.next

    return head

