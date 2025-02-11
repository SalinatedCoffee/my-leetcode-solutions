class Solution:
  def removeOccurrences(self, s: str, part: str) -> str:
    # brute force

    while part in s:
      idx = s.find(part)
      s = s[:idx] + s[idx+len(part):]

    return s

