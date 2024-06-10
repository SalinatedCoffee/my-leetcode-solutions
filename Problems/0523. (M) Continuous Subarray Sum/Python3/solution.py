class Solution:
  def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    # prefix sums with set

    n = len(nums)

    # sanity check
    if n < 2:
      return False

    # prefix sum of nums[:i-1]
    prefix_mod_lag = 0
    # prefix sum of nums[:i+1]
    prefix_mod = (nums[0] + nums[1]) % k
    if prefix_mod == 0:
      return True
    # mods contains sum(nums[:j]) % k where j < i
    # and i is index of current element
    mods = set()
    mods.add(0)
    for i in range(2, n):
      # update set of prefix sum mod k
      prefix_mod_lag = (prefix_mod_lag + nums[i-2]) % k
      mods.add(prefix_mod_lag)
      # comptute prefix sum including current element
      prefix_mod = (prefix_mod + nums[i]) % k
      if prefix_mod in mods:
        return True

    return prefix_mod in mods

