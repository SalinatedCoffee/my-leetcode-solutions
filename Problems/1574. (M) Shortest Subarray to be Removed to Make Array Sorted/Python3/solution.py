class Solution:
  def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
    # two pointers

    n = len(arr)
    l, h = 0, n-1
    # find the index of the first element
    # of the longest increasing suffix of arr
    for i in range(n-2, -1, -1):
      if arr[i] <= arr[i+1]:
        h = i
      else:
        break

    # worst case is when entirety of prefix is non-increasing
    res = h
    # for every element in the non-decreasing prefix of arr...
    while l < h and (l == 0 or arr[l-1] <= arr[l]):
      # find the first element in the suffix greater than or equal to it
      while h < n and arr[l] > arr[h]:
        h += 1
      res = min(res, h - l - 1)
      l += 1

    return res

