class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    # recursive approach, if valid either include or don't include number
    self.ret = []
    self.ans = []

    def recurse(current):
      if current >= len(nums):
        # check if current subsequence is valid
        if len(self.ans) >= 2:
          self.ret.append(self.ans[:])
        return
      if self.ans and nums[current] >= self.ans[-1]:
        # check for possible duplicates before recursion
        if nums[current] != self.ans[-1]:
          recurse(current+1)
        self.ans.append(nums[current])
        recurse(current+1)
        self.ans.pop()
        return
      elif not self.ans:
        recurse(current+1)
        self.ans.append(nums[current])
        recurse(current+1)
        self.ans.pop()
      # current is smaller than last number in subsequence
      else:
        recurse(current+1)
      return

    recurse(0)

    return self.ret

