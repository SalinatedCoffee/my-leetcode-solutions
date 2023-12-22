class Solution:
  def countSubstrings(self, s: str) -> int:
    # Manacher's algorithm

    # interleave s to handle even-length palindromes
    s_i = '0' + "".join('|' + c for c in s) + "|1"
    n = len(s_i)

    # rad[i] is radius of palindrome centered at i (including i)
    rad = [0] * n
    l, r = 1, 1
    for i in range(1, n - 1):
      rad[i] = max(0, min(r - i, rad[l + (r - i)]))
      while i - rad[i] >= 0 and i + rad[i] < n and s_i[i - rad[i]] == s_i[i + rad[i]]:
        rad[i] += 1
      if i + rad[i] > r:
        l, r = i - rad[i], i + rad[i]

    # count number of palindromic substrings in s
    return sum([rad[i] // 2 for i in range(2, n)])

