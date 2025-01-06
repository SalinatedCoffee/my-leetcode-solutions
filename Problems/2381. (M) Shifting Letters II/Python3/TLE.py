class Solution:
  def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
    # brute force
    
    n = len(s)
    # apply shifts
    char_shift = [0] * n
    for i, j, k in shifts:
      d = 1 if k else -1
      for idx in range(i, j+1):
        char_shift[idx] += d
    
    # reconstruct resulting string
    res = []
    for idx, shift in enumerate(char_shift):
      shift += ord(s[idx]) - ord('a')
      shift %= len(string.ascii_lowercase)
      res.append(chr((shift + len(string.ascii_lowercase)) % len(string.ascii_lowercase) + ord('a')))

    return ''.join(res)

