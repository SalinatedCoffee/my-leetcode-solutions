class Solution:
  def minimumLength(self, s: str) -> int:
    # two pointers
    
    n = len(s)
    l, r = 0, n-1
    ret = n
    while l < r and s[l] == s[r]:
      c = s[l]
      while l <= r and s[l] == c:
        l += 1
      while r > l and s[r] == c:
        r -= 1

    return r - l + 1

