class Solution:
  def beautifulSubsets(self, nums: List[int], k: int) -> int:
    # backtracking

    n = len(nums)
    cur = Counter()
    
    def recurse(idx):
      # return number of valid subsets of nums[idx:]
      # reached end of list, count subset if it is not empty
      if idx == n:
        return 1 if len(cur) else 0
      ret = 0
      # if nums[idx] can be added to subset, try adding it
      if nums[idx] + k not in cur and nums[idx] - k not in cur:
        cur[nums[idx]] += 1
        ret += recurse(idx + 1)
        cur[nums[idx]] -= 1
        if cur[nums[idx]] == 0:
          del cur[nums[idx]]
      # try skipping nums[idx]
      ret += recurse(idx + 1)

      return ret

    return recurse(0)

