class Solution:
  def numFactoredBinaryTrees(self, arr: List[int]) -> int:
    # top-down dynamic programming (memoization) on pre-sorted input

    n = len(arr)
    # sort arr in-place, in descending order
    arr.sort(reverse=True)
    # arr_dict[v] is index of value v within sorted arr
    arr_dict = {v:i for i,v in enumerate(arr)}
    mod = 10**9 + 7

    @cache
    # returns number of ways to construct tree rooted at arr[i], using arr[i+1:]
    def recurse(i):
      ret = 1
      for j in range(i+1, n):
        b = arr[i] // arr[j]
        if arr[i] % arr[j] == 0 and b in arr_dict:
          ways = recurse(j) * recurse(arr_dict[b])
          ret += ways
      
      return ret % mod

    ret = 0
    # account for all possible roots
    for l in range(n):
      ret += recurse(l)
      ret %= mod

    return ret

