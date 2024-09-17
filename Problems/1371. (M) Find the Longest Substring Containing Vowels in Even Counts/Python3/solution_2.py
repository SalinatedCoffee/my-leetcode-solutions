class Solution:
  def findTheLongestSubstring(self, s: str) -> int:
    # bitmasks with dictionary

    n = len(s)
    ctoi = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
    # seen[i] is earliest index j where s[:j+1] contains odd/even number of vowels
    # where each binary bit of i corresponds to the mapping defined by ctoi
    # bit is raised if s[:j+1] contains an odd number of that vowel
    seen = [-2] * 2**5
    seen[0] = -1
    res = 0
    cur_counts = 0

    # determine length of longest valid substring
    for i in range(n):
      # update current bitmask
      if s[i] in ctoi:
        cur_counts ^= 1 << ctoi[s[i]]
      # update length if necessary
      if seen[cur_counts] != -2:
        res = max(res, i - seen[cur_counts])
      else:
        seen[cur_counts] = i
    
    return res

