class Solution:
  def subsets(self, nums: List[int]) -> List[List[int]]:
    # recursion

    n = len(nums)
    ret = []
    cur = []
    def recurse(i):
      if i == n:
        ret.append(cur[:])
        return
      recurse(i+1)
      cur.append(nums[i])
      recurse(i+1)
      cur.pop()

    recurse(0)

    return ret

