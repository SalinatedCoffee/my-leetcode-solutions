class Solution:
  def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
    # top-down dynamic programming (memoization)
    
    n = len(s)

    @cache
    def recurse(i, k, prev, prev_run):
      # return minimum length of compressing s[i:] given k deletions
      # where previous character is prev with a run length of prev_run

      # previously deleted when no deletions remained
      if k < 0:
        return float('inf')
      # reached end of string or all remaining characters are removable
      if i == n - k:
        return 0
      # current char is same as previous
      if s[i] == prev:
        # if compressed run increases in length, adjust accordingly
        cmpr = 1 if prev_run in [1, 9, 99] else 0
        # don't delete s[i]
        ret = cmpr + recurse(i + 1, k, prev, prev_run + 1)
      # current char is different to previous
      else:
        # try deleting or not deleting s[i], select optimal choice
        ret = min(recurse(i + 1, k - 1, prev, prev_run),
        # prev character is different, so add compressed length
          1 + recurse(i + 1, k, s[i], 1))
      
      return ret

    return recurse(0, k, '', 0)

