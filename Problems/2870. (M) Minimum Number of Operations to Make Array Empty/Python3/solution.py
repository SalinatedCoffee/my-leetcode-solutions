class Solution:
  def minOperations(self, nums: List[int]) -> int:
    # greedy with dictionary
    
    ret = 0
    freq = Counter(nums)
    for f in freq.values():
      q, r = f // 3, f % 3
      if not q and r == 1:
        return -1
      ret += q + 1 if r else q

    return ret

