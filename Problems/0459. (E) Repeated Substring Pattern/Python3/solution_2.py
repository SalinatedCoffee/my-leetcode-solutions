class Solution:
  def repeatedSubstringPattern(self, s: str) -> bool:
    # check if string is rotatable

    t = s + s
    if s in t[1:-1]:
      return True
    return False

