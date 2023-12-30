class Solution:
  def makeEqual(self, words: List[str]) -> bool:
    # brute force

    n = len(words)
    freq = [0] * 26
    for word in words:
      for c in word:
        freq[ord(c) - ord('a')] += 1
    
    for f in freq:
      if f % n:
        return False

    return True

