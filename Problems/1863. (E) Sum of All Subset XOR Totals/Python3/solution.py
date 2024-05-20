class Solution:
  def subsetXORSum(self, nums: List[int]) -> int:
    # recursion

    n = len(nums)

    def recurse(idx, xor):
      # return XOR total for nums[idx:] where the current XOR sum is xor
      if idx == n:
        return xor
      return recurse(idx+1, xor) + recurse(idx+1, xor ^ nums[idx])

    return recurse(0, 0)

