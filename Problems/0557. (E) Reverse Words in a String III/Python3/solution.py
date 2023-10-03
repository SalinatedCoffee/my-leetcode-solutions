class Solution:
  def reverseWords(self, s: str) -> str:
    # without str.split()

    n = len(s)
    ret = ""
    idx = 0
    for i in range(n):
      if s[i] == ' ':
        ret += s[idx:i][::-1] + ' '
        idx = i + 1
    
    return ret + s[idx:][::-1]

