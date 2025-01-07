class Solution:
  # KMP pattern matching

  def stringMatching(self, words: List[str]) -> List[str]:
    n = len(words)
    res = []
    for i in range(n):
      lps = self._compute_lps(words[i])
      for j in range(n):
        if i != j and self._is_substring_of(words[i], words[j], lps) is True:
          res.append(words[i])
          break

    return res

  # compute and return longest proper prefix/suffix array for string s
  def _compute_lps(self, s):
    lps = [0] * len(s)
    idx, cur_len = 1, 0
    while idx < len(s):
      if s[idx] == s[cur_len]:
        cur_len += 1
        lps[idx] = cur_len
        idx += 1
      else:
        if cur_len > 0:
          cur_len = lps[cur_len - 1]
        else:
          idx += 1

    return lps

  # determine whether s1 is a substring of s2 using KMP
  def _is_substring_of(self, s1, s2, lps):
    idx1, idx2 = 0, 0
    while idx2 < len(s2):
      if s2[idx2] == s1[idx1]:
        idx1 += 1
        idx2 += 1
        if idx1 == len(s1):
          return True
      else:
        if idx1 > 0:
          idx1 = lps[idx1 - 1]
        else:
          idx2 += 1

    return False

