class Solution:
  def grayCode(self, n: int) -> List[int]:
    # recursion

    # base case
    if n == 1:
      return [0, 1]

    # define prefix
    prefix = 1 << n-1
    # create reversed copy of Gray codes for n-1
    prev = self.grayCode(n-1)
    prev_rev = prev[::-1]
    # attach prefix to reversed copy
    for i in range(len(prev_rev)):
      prev_rev[i] |= prefix

    # return contatenated list
    return prev + prev_rev

