class Solution:
  def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
    # pre-sort arr2
    # top-down dynamic programming (memoization) with binary search

    n = len(arr1)
    arr2.sort()
    # dp[(i, j)] is return value of recurse(i, j)
    dp = {}
    
    # return minimum operations to make arr1[i:] strictly increasing
    # where prev = arr1[i-1] if i else -1
    def recurse(i, prev):
      if i == n:
        return 0
      if (i, prev) in dp:
        return dp[(i, prev)]
      cost = float('inf')
      # already strictly increasing, try leaving arr1[i] as is
      if arr1[i] > prev:
        cost = recurse(i+1, arr1[i])
      idx = bisect.bisect_right(arr2, prev)
      # if more optimal value exists in arr2, try using that
      if idx < len(arr2):
        cost = min(cost, 1+recurse(i+1, arr2[idx]))
      dp[(i, prev)] = cost
      
      return cost
  
    return ret if (ret := recurse(0, -1)) != float('inf') else -1

