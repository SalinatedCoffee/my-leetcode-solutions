class Solution:
  def partitionString(self, s: str) -> int:
    # greedy

    cur = set()
    ret = 0
    for c in s:
      if c not in cur:
        cur.add(c)
      else:
        ret += 1
        cur.clear()
        cur.add(c)
    
    return ret if not cur else ret + 1

