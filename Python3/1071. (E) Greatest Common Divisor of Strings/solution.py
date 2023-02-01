class Solution:
  def gcdOfStrings(self, str1: str, str2: str) -> str:
    # brute force - try all possible prefixes
    l1, l2 = len(str1), len(str2)
    res = ""
    for i in range(min(l1, l2)):
      # mismatching characters, break early
      if str1[i] != str2[i]:
        break
      # string(s) not divisible by prefix
      elif l1 % (i+1) != 0 or l2 % (i+1) != 0:
        continue

      prefix = str1[0:i+1]
      s1, s2 = True, True
      # see if strings divisible by prefix
      for j in range(i+1, l1, i+1):
        if str1[j:j+i+1] != prefix:
          s1 = False
          break
      for j in range(i+1, l2, i+1):
        if str2[j:j+i+1] != prefix:
          s2 = False
          break

      if s1 and s2:
        res = prefix
      
    return res

