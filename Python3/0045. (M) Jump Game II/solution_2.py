class Solution:
  def jump(self, nums: List[int]) -> int:
    # greedy solution

    # sanity check
    if len(nums) == 1:
      return 0

    jumps = 0
    # intvl is range of currently traversed interval
    # reach is range of next traversable interval
    intvl, reach = 0, 0
    for i in range(len(nums)-1):
      # update next interval range
      reach = max(reach, i+nums[i])
      # end of current interval
      if i == intvl:
        jumps += 1
        intvl = reach

    return jumps

