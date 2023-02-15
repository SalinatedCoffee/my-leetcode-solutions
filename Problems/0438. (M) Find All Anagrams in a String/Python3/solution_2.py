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
    
    match = 0
    for i in range(26):
      if cnt_p[i] == cnt_s[i]:
        match += 1

    res = []
    i, j = 0, len(p)
    while j < len(s):
      # if match, append i
      if match == 26:
        res.append(i)
      idx_i, idx_j = ctoi(s[i]), ctoi(s[j])
      # advance left
      cnt_s[idx_i] -= 1
      if cnt_p[idx_i] == cnt_s[idx_i]:
        match += 1
      elif cnt_p[idx_i] == cnt_s[idx_i] + 1:
        match -= 1
      # advance right
      cnt_s[idx_j] += 1
      if cnt_p[idx_j] == cnt_s[idx_j]:
        match += 1
      elif cnt_p[idx_j] == cnt_s[idx_j] - 1:
        match -= 1
      i += 1
      j += 1
    
    # check match for s[-len(p):] (or potentially s[:len(p)])
    if match == 26:
      res.append(i)

    return res

