class Solution:
  def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    # recursive approach, if valid either include or don't include number
    self.ret = []
    self.ans = []
    self.seen = set()

    def recurse(current):
      if current >= len(nums):
        # check if current subsequence is valid and unique
        if len(self.ans) >= 2 and tuple(self.ans) not in self.seen:
          self.seen.add(tuple(self.ans))
          self.ret.append(self.ans[:])
        return
      # recurse twice, with and without current number
      if not self.ans or nums[current] >= self.ans[-1]:
        recurse(current+1)
        self.ans.append(nums[current])
        recurse(current+1)
        self.ans.pop()
        return
      # current is smaller than last number in subsequence
      else:
        recurse(current+1)

      return

    recurse(0)

    return self.ret

