class Solution:
  # modified quickselect

  def findKthLargest(self, nums: List[int], k: int) -> int:

    return self.qs(nums, k)

  
  def qs(self, nums, k):
    pivot = nums[-1]
    l, m, r = [], [], []
    for n in nums:
      if pivot < n:
        l.append(n)
      elif pivot > n:
        r.append(n)
      else:
        m.append(n)
        
    if len(l) >= k:
      return self.qs(l, k)
    if len(l) + len(m) < k:
      return self.qs(r, k - len(l) - len(m))

    return pivot

