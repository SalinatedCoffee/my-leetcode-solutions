class Solution:
  def isArraySpecial(self, nums: List[int]) -> bool:
    # brute force using modulo

    n = len(nums)
    for i in range(1, n):
      # if the iterpreter is smart, it will replace the modulo operation with a bit masking operation
      if nums[i-1] % 2 == nums[i] % 2:
        return False

    return True

