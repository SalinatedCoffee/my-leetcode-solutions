class Solution:
  def isAlienSorted(self, words: List[str], order: str) -> bool:
    # create mapping list
    # compare one by one, if different len and identical shorter comes first
    
    # generate mapping
    mapping = [0] * len(string.ascii_lowercase)
    ctoi = lambda x: ord(x) - 97
    ntoa = lambda x: mapping[ctoi(x)]
    for i in range(len(order)):
      mapping[ctoi(order[i])] = i
    
    for i in range(1, len(words)):
      w1, w2 = words[i-1], words[i]
      l1, l2 = len(w1), len(w2)
      skip = False
      for j in range(min(l1, l2)):
        # words[i-1] is lex. greater than words[i]
        if ntoa(w1[j]) > ntoa(w2[j]):
          return False
        # words[i-1] is lex. less than words[i]
        elif ntoa(w1[j]) < ntoa(w2[j]):
          skip = True
          break
      # words lex. equal up to min(l1, l2), but words[i-1] is longer
      if not skip and l1 > l2:
        return False
    
    return True

