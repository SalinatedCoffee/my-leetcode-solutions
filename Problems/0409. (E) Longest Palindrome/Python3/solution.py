class Solution:
  def longestPalindrome(self, s: str) -> int:

    n = len(s)
    # count frequency of each unique letter
    freq = Counter(s)

    ret = 0
    odd = 0
    # compute length of halved palindrome
    for f in freq.values():
      ret += f // 2
      odd |= f & 1

    # if at least one letter has an odd frequency, make it the center
    return ret * 2 + odd

