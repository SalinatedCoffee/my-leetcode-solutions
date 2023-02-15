class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:
    # sliding window
    # maintain letter count, add left-side index to result on match

    # sanity check
    if len(p) > len(s):
      return []
    
    # count letters in p and s[0:len(p)]
    cnt_p = [0] * 26
    cnt_s = [0] * 26
    ctoi = lambda x: ord(x) - 97
    for i in range(len(p)):
      cnt_p[ctoi(p[i])] += 1
      cnt_s[ctoi(s[i])] += 1

    # helper function that checks if letter counts match
    def verify(a, b):
      for i in range(len(a)):
        if a[i] != b[i]:
          return False
      return True
    
    res = []
    i, j = 0, len(p)
    while j < len(s):
      # if match, append i
      if verify(cnt_p, cnt_s):
        res.append(i)
      # advance window
      cnt_s[ctoi(s[i])] -= 1
      cnt_s[ctoi(s[j])] += 1
      i += 1
      j += 1
    
    # check match for s[-p:]
    if verify(cnt_p, cnt_s):
      res.append(i)

    return res

