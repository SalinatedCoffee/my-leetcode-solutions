class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    # reverse traversal

    ret = 0
    # skip trailing whitespace
    i = len(s) - 1
    while i >= 0 and s[i] == ' ':
      i -= 1
    # count number of characters in last word
    while i >= 0 and s[i] != ' ':
      i -= 1
      ret += 1

    return ret

