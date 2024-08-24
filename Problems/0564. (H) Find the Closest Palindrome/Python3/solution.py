class Solution:
  def nearestPalindromic(self, n: str) -> str:
    # math

    digits = len(n)
    pivot = digits // 2 - (0 if digits % 2 else 1)
    # extract first half of n as integer
    half = int(n[:pivot+1])

    # return mirrored palindrome using half as the left side,
    # having even digits if even == True
    def palindrome(half, even):
      ret = half
      if even is False:
        half //= 10
      while half > 0:
        ret = ret * 10 + half % 10
        half //= 10
      
      return ret

    # generate candidate palindromes
    cand = []
    cand.append(palindrome(half, digits % 2 == 0))
    cand.append(palindrome(half + 1, digits % 2 == 0))
    cand.append(palindrome(half - 1, digits % 2 == 0))
    cand.append(10**(digits-1) - 1)
    cand.append(10**digits + 1)

    # select candidate closest to n
    d = float('inf')
    ret = 0
    n_int = int(n)
    for c in cand:
      if c == n_int:
        continue
      if abs(c - n_int) < d:
        d = abs(c - n_int)
        ret = c
      elif abs(c - n_int) == d:
        ret = min(ret, c)

    return str(ret)

