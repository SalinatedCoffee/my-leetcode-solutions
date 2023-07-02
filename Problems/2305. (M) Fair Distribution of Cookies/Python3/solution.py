class Solution:
  def distributeCookies(self, cookies: List[int], k: int) -> int:
    # backtracking

    n = len(cookies)
    counts = [0] * k

    def recurse(i, j):
      ret = float('inf')
      if n - i < j:
        return ret
      if i == n:
        return max(counts)
      for l in range(k):
        if not counts[l]:
          j -= 1
        counts[l] += cookies[i]
        ret = min(ret, recurse(i+1, j))
        counts[l] -= cookies[i]
        if not counts[l]:
          j += 1

      return ret
    
    return recurse(0, k)
 
