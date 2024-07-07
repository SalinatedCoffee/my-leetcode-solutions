class Solution:
  def isMatch(self, s: str, p: str) -> bool:
    # top-down dynamic programming (memoization)

    m, n = len(s), len(p)

    @cache
    def recurse(s_idx, p_idx):
      # determine whether p[p_idx] matches against s[s_idx]

      # base case
      if p_idx == n:
        return s_idx == m
      
      # check whether first characters match
      char_match = s_idx < m and p[p_idx] in [s[s_idx], '.']
      # pattern window contains quantifier (Kleene star)
      if p_idx + 1 < n and p[p_idx+1] == '*':
        return recurse(s_idx, p_idx+2) or char_match and recurse(s_idx+1, p_idx)
      # pattern window does not contain quantifier
      else:
        return char_match and recurse(s_idx+1, p_idx+1)

    return recurse(0, 0)

