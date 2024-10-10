class Solution:
  def maxWidthRamp(self, nums: List[int]) -> int:
    # monotonic decreasing stack

    n = len(nums)
    # populate monotonic stack with potential left sides of ramp
    stack = []
    for i, num in enumerate(nums):
      if not stack or stack[-1][1] > num:
        stack.append((i, num))
    
    # determine largest possible ramp width
    res = 0
    for i in range(n-1, -1, -1):
      while stack and stack[-1][1] <= nums[i]:
        res = max(res, i - stack[-1][0])
        stack.pop()

    return res

