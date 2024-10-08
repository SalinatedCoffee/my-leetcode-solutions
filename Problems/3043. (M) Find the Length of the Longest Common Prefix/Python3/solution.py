class Solution:
  def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    # trie

    m, n = len(arr1), len(arr2)
    # generate trie from arr1
    root = {}
    for num in map(str, arr1):
      cur = root
      for c in num:
        if c not in cur:
          cur[c] = {}
        cur = cur[c]
    
    # find length of longest common prefix
    res = 0
    for num in map(str, arr2):
      cur, d = root, 0
      for c in num:
        if c not in cur:
          break
        cur = cur[c]
        d += 1
      res = max(res, d)

    return res

