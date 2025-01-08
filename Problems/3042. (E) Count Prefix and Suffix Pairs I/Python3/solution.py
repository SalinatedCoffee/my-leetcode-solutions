class Solution:
  def countPrefixSuffixPairs(self, words: List[str]) -> int:
    # brute force
    
    # return True if candidate is prefix and suffix of target
    def is_prefix_and_suffix(candidate, target):
      if len(candidate) > len(target):
        return False
      c_len = len(candidate)
      if target[:c_len] == candidate and target[-c_len:] == candidate:
        return True
      return False
    
    n = len(words)
    # count valid pairs
    res = 0
    for i in range(n):
      for j in range(i+1, n):
        if is_prefix_and_suffix(words[i], words[j]):
          res += 1

    return res

