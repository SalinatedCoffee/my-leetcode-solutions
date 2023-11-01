class Solution:
  def countVowelPermutation(self, n: int) -> int:
    # top-down dynamic programming (memoization)
    
    mod = 10**9 + 7
    # vowels are 0-indexed in the order of aeiou
    r_mapping = [[1,2,4], [0,2], [1,3], [2], [2,3]]

    @cache
    # recurse(i,j) returns number of ways to form a string of length n
    #   that ends in the j-th vowel
    def recurse(i, v):
      if i == 1:
        return 1

      ret = 0
      for n_v in r_mapping[v]:
        ret += recurse(i-1, n_v)
      ret %= mod

      return ret

    ans = 0
    for i in range(5):
      ans += recurse(n, i)
      ans %= mod
    
    return ans

