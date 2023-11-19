class Solution:
  def reductionOperations(self, nums: List[int]) -> int:
    # greedy algorithm on sorted list

    n = len(nums)
    nums.sort(reverse=True)
    ret = 0
    for i in range(1, n):
      if nums[i] != nums[i-1]:
        ret += i
    
    return ret

