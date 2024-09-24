class Solution:
  def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
    # brute force

    m, n = len(arr1), len(arr2)
    # convert integers to strings
    arr1_str, arr2_str = map(str, arr1), list(map(str, arr2))
    res = 0
    # find length of longest common prefix
    for i in arr1_str:
      for j in arr2_str:
        k = 0
        while k < len(i) and k < len(j) and i[k] == j[k]:
          k += 1
        res = max(res, k)

    return res

