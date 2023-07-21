class Solution:
  def findNumberOfLIS(self, nums: List[int]) -> int:
    # bottom-up dynamic programming (tabulation)

    n = len(nums)
    # length[i] is value of LIS ending at nums[i]
    length = [1] * n
    # count[i] is number of LIS ending at nums[i]
    count = [1] * n

    for i in range(n):
      for j in range(i):
        if nums[j] < nums[i]:
          if length[j] + 1 > length[i]:
            length[i] = length[j] + 1
            count[i] = 0
          if length[j] + 1 == length[i]:
            count[i] += count[j]
    
    ret = 0
    longest = max(length)
    for i in range(n):
      if length[i] == longest:
        ret += count[i]
    
    return ret

