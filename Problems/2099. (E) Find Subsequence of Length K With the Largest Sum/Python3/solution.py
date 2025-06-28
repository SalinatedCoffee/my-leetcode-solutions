class Solution:
  def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
    # sort

    n = len(nums)
    nums = [(nums[i], i) for i in range(n)]
    nums.sort(reverse = True)
    res = nums[:k]
    res.sort(key = lambda x: x[1])

    return [res[i][0] for i in range(k)]

