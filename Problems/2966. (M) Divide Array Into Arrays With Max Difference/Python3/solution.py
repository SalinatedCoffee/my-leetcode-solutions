class Solution:
  def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
    # greedy on sorted array

    n = len(nums)
    # sanity check
    if n % 3:
      return []

    nums.sort()
    ret = []
    for i in range(n//3):
      p = nums[i*3:i*3+3]
      if p[-1] - p[0] > k:
        return []
      ret.append(p)

    return ret

