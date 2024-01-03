class Solution:
  def numberOfBeams(self, bank: List[str]) -> int:
    # math

    ret = 0
    prev, cur = 0, 0
    for row in bank:
      for c in row:
        if c == '1':
          cur += 1
      if cur:
        ret += prev * cur
        prev, cur = cur, 0

    return ret

