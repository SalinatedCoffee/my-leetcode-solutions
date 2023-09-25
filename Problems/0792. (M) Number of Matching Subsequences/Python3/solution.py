class Solution:
  def numMatchingSubseq(self, s: str, words: List[str]) -> int:
    # dynamic programming

    # l2w[c] is list of words starting with character c
    #   where a word is represented by a tuple (i, j)
    #   word = words[i][j:]
    l2w = defaultdict(list)
    for i, word in enumerate(words):
      l2w[word[0]].append((i, 0))
    
    ret = 0
    for c in s:
      l_words = l2w[c]
      l2w[c] = []
      for word, idx in l_words:
        if idx == len(words[word]) - 1:
          ret += 1
        else:
          l2w[words[word][idx+1]].append((word, idx+1))
    
    return ret

