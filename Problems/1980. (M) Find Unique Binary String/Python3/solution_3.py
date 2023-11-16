class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    # math (Cantor's diagonal argument)

    n = len(nums)
    ret = [None] * n
    for i in range(n):
      ret[i] = "0" if nums[i][i] == "1" else "1"
    
    return "".join(ret)

