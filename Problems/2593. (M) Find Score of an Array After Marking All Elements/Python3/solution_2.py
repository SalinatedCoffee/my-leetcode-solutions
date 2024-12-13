class Solution:
  def findScore(self, nums: List[int]) -> int:
    # monotonic decreasing stack

    n = len(nums)
    stack = []
    res = 0
    for num in nums:
      if not stack or num < stack[-1]:
        stack.append(num)
      # if current element is larger than top of stack, empty entire stack
      else:
        while stack:
          res += stack.pop()
          if stack:
            stack.pop()

    while stack:
      res += stack.pop()
      if stack:
        stack.pop()

    return res

