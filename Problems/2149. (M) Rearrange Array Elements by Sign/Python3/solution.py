class Solution:
  def rearrangeArray(self, nums: List[int]) -> List[int]:
    # double queues

    pos, neg = deque(), deque()
    for num in nums:
      if num < 0:
        neg.append(num)
      else:
        pos.append(num)
    
    ret = []
    while pos:
      ret.append(pos.popleft())
      ret.append(neg.popleft())

    return ret

