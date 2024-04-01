class Solution:
  def lengthOfLastWord(self, s: str) -> int:
    # split by whitespace and reverse word with Python builtins

    words = s.split(' ')
    for word in reversed(words):
      if word != '':
        return len(word)

    # this line should never execute given problem constraints
    return -1

