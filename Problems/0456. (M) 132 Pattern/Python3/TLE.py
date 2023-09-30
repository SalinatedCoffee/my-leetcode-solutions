class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    # brute force

    n = len(nums)
    known_min = float('inf')
    for j in range(n-1):
      known_min = min(known_min, nums[j])
      for k in range(j+1, n):
        if known_min < nums[k] < nums[j]:
          return True

    return False

