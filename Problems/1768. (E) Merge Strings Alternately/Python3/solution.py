class Solution:
  def mergeAlternately(self, word1: str, word2: str) -> str:
    # two pointers

    p1, p2 = 0, 0
    ret = ""
    while p1 < len(word1) and p2 < len(word2):
      if len(ret) % 2:
        ret += word2[p2]
        p2 += 1
      else:
        ret += word1[p1]
        p1 += 1
    
    if p1 < len(word1):
      ret += word1[p1:]
    elif p2 < len(word2):
      ret += word2[p2:]
    return ret

