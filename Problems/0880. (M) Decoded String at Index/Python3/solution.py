class Solution:
  def decodeAtIndex(self, s: str, k: int) -> str:
    # reverse traversal

    n = len(s)
    tape_len, idx = 0, 0
    # only consider substring that would include k
    while tape_len < k:
      if s[idx].isalpha():
        tape_len += 1
      else:
        tape_len *= int(s[idx])
      idx += 1
        
    # step through substring in reverse
    for j in range(idx-1, -1, -1):
      c = s[j]
      if c.isalpha():
        if k == 0 or k == tape_len:
          return c
        tape_len -= 1
      else:
        tape_len //= int(c)
        k %= tape_len

    # this line should never run
    return ''

