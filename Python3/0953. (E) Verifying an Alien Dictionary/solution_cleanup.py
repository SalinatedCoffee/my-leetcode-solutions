class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    # create mapping list
    # compare one by one, if different len and identical shorter comes first
    
    # generate mapping
    mapping = {}
    for i in range(len(order)):
      mapping[order[i]] = i
    
    for i in range(len(words)-1):
      for j in range(len(words[i])):
        # no mismatch found and current word is longer than next
        if j >= len(words[i+1]):
          return False
        # mismatch found
        if words[i][j] != words[i+1][j]:
          # current is lex. greater than next
          if mapping[words[i][j]] > mapping[words[i+1][j]]:
            return False
          # current is lex. less than next
          break
    
    return True

