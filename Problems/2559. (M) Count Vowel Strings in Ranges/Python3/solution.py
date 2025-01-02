class Solution:
  def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    # prefix sums

    n = len(words)
    VOWELS = "aeiou"
    # value of pre[i] is number of valid strings in words[:i+1]
    pre = [0] * n
    cur = 0
    for i in range(n):
      if words[i][0] in VOWELS and words[i][-1] in VOWELS:
        cur += 1
      pre[i] = cur
    
    # process queries using precomputed prefix sums
    res = []
    for l, h in queries:
      l = l if l == 0 else pre[l-1]
      res.append(pre[h] - l)

    return res

