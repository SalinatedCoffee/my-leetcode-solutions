class Solution:
  def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
    # compare contatenations
    
    return ''.join(word1) == ''.join(word2)

