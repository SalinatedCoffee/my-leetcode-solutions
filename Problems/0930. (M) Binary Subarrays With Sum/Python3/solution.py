class Solution:
  def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
    # prefix sums with dictionary

    n = len(nums)
    # psum_counts[i] is number of prefix subarrays that sum to i
    psum_counts = defaultdict(int)
    psum_counts[0] = 1
    ret = 0
    prefix_sum = 0
    for num in nums:
      prefix_sum += num
      if prefix_sum >= goal:
        ret += psum_counts[prefix_sum - goal]
      psum_counts[prefix_sum] += 1
    
    return ret

