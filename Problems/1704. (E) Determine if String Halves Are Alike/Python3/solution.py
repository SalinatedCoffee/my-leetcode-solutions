class Solution:
  def halvesAreAlike(self, s: str) -> bool:
    # simple iteration

    n = len(s)
    m = n // 2
    vowels = "aeiouAEIOU"

    c = 0
    for i in range(m):
      if s[i] in vowels:
        c += 1
      if s[m+i] in vowels:
        c -= 1

    return c == 0

