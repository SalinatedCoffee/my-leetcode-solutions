class Solution:
  def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
    # dictionary

    # generate smallest set of characters that is a superset of each word in words2
    superset = Counter()
    for word in words2:
      cur_set = Counter(word)
      for k, v in cur_set.items():
        superset[k] = max(superset[k], v)
    
    # count words in words1 that is a superset of all words in words2
    res = []
    for word in words1:
      cur_set = Counter(word)
      universal = True
      for k, v in superset.items():
        if v > cur_set[k]:
          universal = False
          break
      if universal:
        res.append(word)

    return res

