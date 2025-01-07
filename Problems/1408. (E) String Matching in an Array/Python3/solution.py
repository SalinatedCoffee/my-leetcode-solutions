class Solution:
  def stringMatching(self, words: List[str]) -> List[str]:
    # brute force

    n = len(words)
    res = []
    for i in range(n):
      for j in range(n):
        if i != j and words[i] in words[j]:
          res.append(words[i])
          break

    return res

