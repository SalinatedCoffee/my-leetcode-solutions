class Solution:
  def takeCharacters(self, s: str, k: int) -> int:
    # sliding window

    n = len(s)

    # window is valid if the expression
    # frequency of c in s - frequency of c in window >= l
    # evaluates to True for each unique character c in s
    verify = lambda freq, w_freq: \
      freq[0] - w_freq[0] >= k \
      and freq[1] - w_freq[1] >= k \
      and freq[2] - w_freq[2] >= k

    # count frequency of each unique character in s
    freq = [0] * 3
    for c in s:
      freq[ord(c) - ord('a')] += 1
    # sanity check
    if verify(freq, [0, 0, 0]) is False:
      return -1

    w_freq = [0] * 3
    res, l = 0, 0
    for i in range(n):
      w_freq[ord(s[i]) - ord('a')] += 1
      # if window is invalid, shrink window from the left
      while l <= i and verify(freq, w_freq) is False:
        w_freq[ord(s[l]) - ord('a')] -= 1
        l += 1
      res = max(res, i - l + 1)

    return n - res

