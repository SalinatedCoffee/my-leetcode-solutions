class Solution:
  def findDifferentBinaryString(self, nums: List[str]) -> str:
    # hash

    n = len(nums)
    dec = set([int(b, base=2) for b in nums])
    i = 0
    while True:
      if i not in dec:
        break
      i += 1

    return f"{i:b}".rjust(n, "0")

