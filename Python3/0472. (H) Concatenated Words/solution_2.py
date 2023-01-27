class Solution:
  def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
    # store all words in set instead of trie
    # for all words, iterate and see if substring is in set
    # if true, mark end of substring as valid concat

    # cast word list into set for fast lookup
    bag = set(words)
    res = []

    for word in words:
      # init dp data structure
      dp = [0] * (len(word)+1)
      # 0-th element represents prefix of empty string
      dp[0] = 1
      for i in range(len(word)):
        # current index is not end of valid concat
        if not dp[i]:
          continue
        # all substrings of range [i+1,len(word)]
        for j in range(i+1, len(word)+1):
          # if substring is not entire word and exists in word set
          if j-i < len(word) and word[i:j] in bag:
            # mark end of substring as end of valid concat
            dp[j] = 1
        # if entire word is valid concat
        if dp[len(word)]:
          res.append(word)
          break
    
    return res

