class Solution:
  def maximumLength(self, s: str) -> int:
    # brute force using dictionary

    n = len(s)
    freq = defaultdict(int)
    # generate all possible substrings
    for i in range(1, n+1):
      for j in range(n-i+1):
        substr = s[j:j+i]
        # only count substring if it is special
        for c in substr:
          if substr[0] != c:
            substr = ""
            break
        freq[substr] += 1

    # determine length of longest valid substring
    res = 0
    for k, v in freq.items():
      if v >= 3:
        res = max(res, len(k))
    
    return res if res > 0 else -1

