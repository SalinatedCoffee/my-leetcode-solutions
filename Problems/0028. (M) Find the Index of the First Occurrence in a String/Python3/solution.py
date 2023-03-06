class Solution:
  def strStr(self, haystack: str, needle: str) -> int:
    # naive solution

    # sanity checks
    if not needle:
      return 0
    elif not haystack:
      return -1
    elif len(needle) > len(haystack):
      return -1
        
    found = False
    
    # check against substrings starting at every letter in haystack
    for i in range(len(haystack) - len(needle) + 1):
      for j in range(len(needle)):
        found = True
        if haystack[i+j] != needle[j]:
          found = False
          break
      if found:
        return i
            
    return -1

