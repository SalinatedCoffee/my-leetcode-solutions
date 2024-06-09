class Solution:
  def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
    # recursive backtracking

    n = len(s)
    wd_hash = set(wordDict)
    ret = []
    # current list of partitioned words
    words = []

    def recurse(idx):
      # if end of string is reached
      if idx == n:
        ret.append(' '.join(words))
        return
      # otherwise, try all possible partitionings
      for i in range(idx, n):
        # if word in dictionary
        if s[idx:i+1] in wd_hash:
          words.append(s[idx:i+1])
          recurse(i+1)
          words.pop()

    recurse(0)

    return ret

