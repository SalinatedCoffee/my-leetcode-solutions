class Solution:
  def minSubarray(self, nums: List[int], p: int) -> int:
    # optimized prefix sums using dictionary

    n = len(nums)
    # determine mod p of entire array and check for edge case
    tgt = sum(nums) % p
    if tgt == 0:
      return 0
    # idx[i] is largest index j where sum(nums[:j]) % p == i
    idx = {0:-1}
    cur = 0
    res = n
    for i in range(n):
      # update prefix sum modulo p up to current element
      cur = (cur + nums[i]) % p
      # determine whether shorter prefix with equal prefix sum modulo p exists
      if (cur - tgt) % p in idx:
        # if so, update shortest length accordingly
        res = min(res, i - idx[(cur - tgt) % p])
      # update index of current prefix sum modulo p
      idx[cur] = i

    return -1 if res == n else res

