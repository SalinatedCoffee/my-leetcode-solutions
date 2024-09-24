class Solution:
  def findKthNumber(self, n: int, k: int) -> int:
    # simulated trie

    cur = 1
    k -= 1
    # count the number of values between a and b
    #   in the lexicographically ordered list of integers in the range [1, n]
    def count(a, b):
      res = 0
      while a <= n:
        res += min(n+1, b) - a
        a *= 10
        b *= 10

      return res
    
    while k:
      nums = count(cur, cur+1)
      # less values than remaining, skip these values
      if nums <= k:
        cur += 1
        k -= nums
      else:
        cur *= 10
        k -= 1

    return cur

