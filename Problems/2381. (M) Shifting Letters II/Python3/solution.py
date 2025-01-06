class Solution:
  def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    # prefix sum
    
    n = len(s)
    # apply shifts
    deltas = [0] * (n+1)
    for i, j, k in shifts:
      d = 1 if k else -1
      deltas[i] += d
      deltas[j+1] -= d
    
    # reconstruct resulting string
    res = []
    shift = 0
    for i in range(n):
      shift += deltas[i]
      cur = shift + ord(s[i]) - ord('a')
      cur %= len(ascii_lowercase)
      cur += len(ascii_lowercase)
      cur %= len(ascii_lowercase)
      res.append(chr(cur + ord('a')))

    return ''.join(res)

