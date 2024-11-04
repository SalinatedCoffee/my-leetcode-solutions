class Solution:
  def isCircularSentence(self, sentence: str) -> bool:
    # implementation

    words = list(sentence.split())
    n = len(words)
    for i in range(n):
      if words[i-1][-1] != words[i][0]:
        return False

    return True

