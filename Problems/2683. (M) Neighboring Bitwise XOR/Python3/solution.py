class Solution:
  def doesValidArrayExist(self, derived: List[int]) -> bool:
    # bit manipulation

    return reduce(lambda x, y: x ^ y, derived) == 0

