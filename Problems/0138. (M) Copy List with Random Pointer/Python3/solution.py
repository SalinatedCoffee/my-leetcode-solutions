class Solution:
  def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
    # 1-pass solution

    # sanity check
    if head is None:
      return head

    # interleave copied nodes with original
    cur = head
    while cur is not None:
      cur.next = Node(cur.val, cur.next, cur.random)
      cur = cur.next.next
    cur = head

    # make .random of copied nodes point to copied node
    cur = head
    while cur is not None:
      cur_copy = cur.next
      cur_copy.random = cur_copy.random.next if cur_copy.random is not None else None
      cur = cur_copy.next

    # unzip linked list
    cur = head
    ret = cur.next
    while cur is not None:
      cur_copy = cur.next
      cur.next = cur_copy.next
      cur_copy.next = cur.next.next if cur.next is not None else None
      cur = cur.next

    return ret

