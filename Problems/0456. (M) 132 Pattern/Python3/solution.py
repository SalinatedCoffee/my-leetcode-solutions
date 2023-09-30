class Solution:
  def find132pattern(self, nums: List[int]) -> bool:
    # stack

    # sanity check
    if len(nums) < 3:
      return False

    n = len(nums)
    mins = [0] * n
    known_min = float('inf')
    for i in range(n):
      known_min = min(known_min, nums[i])
      mins[i] = known_min

    # for some index j, contains all candidate ks
    #   in nums[j:] in descending order
    k_stack = []
    for j in range(n-1, -1, -1):
      if nums[j] <= mins[j]:
        continue
      while k_stack and k_stack[-1] <= mins[j]:
        k_stack.pop()
      if k_stack and k_stack[-1] < nums[j]:
        return True
      k_stack.append(nums[j])

    return False

