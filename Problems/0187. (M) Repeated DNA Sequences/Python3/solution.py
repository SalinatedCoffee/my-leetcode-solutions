class Solution:
  def findRepeatedDnaSequences(self, s: str) -> List[str]:
    # brute force using dictionary
    
    n = len(s)
    # seen[i] is number of times substring i has been seen in s
    seen = defaultdict(int)
    # count appearance of all 10-long substrings
    for i in range(10, n+1):
      seen[s[i-10:i]] += 1
    
    ret = []
    # return substrings that appear more than once
    for k, v in seen.items():
      if v > 1:
        ret.append(k)

    return ret

