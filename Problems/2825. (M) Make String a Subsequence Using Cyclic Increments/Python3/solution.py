class Solution:
  def canMakeSubsequence(self, str1: str, str2: str) -> bool:
    # two pointers

    m, n = len(str1), len(str2)

    # precompute cyclic increment of each letter
    char_incr = {c: chr((ord(c)-ord('a')+1)%26 + ord('a')) for c in string.ascii_lowercase}
    # index of current character to match in str2
    idx = 0
    for c in str1:
      if str2[idx] == c or str2[idx] == char_incr[c]:
        idx += 1
      if idx == n:
        return True

    return False

