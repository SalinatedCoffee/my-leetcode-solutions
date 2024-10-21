class Solution:
  def maxUniqueSplit(self, s: str) -> int:
    # backtracking with set
    
    n = len(s)
    # previously split substrings
    substrings = set()
    def recurse(idx):
      # base case
      if idx == n:
        return len(substrings)
      
      # try all possible splits for current suffix
      res = 0
      for i in range(idx+1, n+1):
        if s[idx:i] not in substrings:
          substrings.add(s[idx:i])
          res = max(res, recurse(i))
          substrings.remove(s[idx:i])
      
      return res

    return recurse(0)

