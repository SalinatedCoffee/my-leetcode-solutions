class Solution:
  def heightChecker(self, heights: List[int]) -> int:
    # sort

    # just sort heights to get expected
    expected = sorted(heights)
    ret = 0
    for h, e in zip(heights, expected):
      if h != e:
        ret += 1

    return ret

