class Solution:
  def longestStrChain(self, words: List[str]) -> int:
    # bottom-up dynamic programming

    # d_words[word] is longest chain length ending in word
    d_words = {word: 1 for word in words}
    words.sort(key=lambda x: len(x))

    for word in words:
      m = len(word)
      for i in range(m):
        pred = word[:i] + word[i+1:]
        if pred in d_words:
          d_words[word] = max(d_words[word], d_words[pred]+1)
    
    return max(d_words.values())

