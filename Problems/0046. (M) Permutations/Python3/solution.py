class Solution:
  # backtracking

  def permute(self, nums: List[int]) -> List[List[int]]:
    self.n = len(nums)
    self.ret = []
    self.recurse([], set(nums))

    return self.ret
  
  def recurse(self, l_nums, s_nums):
    if self.n == len(l_nums):
      self.ret.append(copy.copy(l_nums))
    else:
      for i in s_nums:
        nxt = copy.copy(s_nums)
        nxt.remove(i)
        l_nums.append(i)
        self.recurse(l_nums, nxt)
        l_nums.pop()

