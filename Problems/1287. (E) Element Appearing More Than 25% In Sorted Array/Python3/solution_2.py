class Solution:
  def findSpecialInteger(self, arr: List[int]) -> int:
    # brute force using sliding window

    tgt = len(arr) / 4
    l = 0
    for i in range(len(arr)):
      if arr[l] != arr[i]:
        if i - l > tgt:
          return arr[l]
        l = i

    return arr[0] if l == 0 else arr[-1]

