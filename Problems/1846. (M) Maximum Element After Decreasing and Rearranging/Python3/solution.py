class Solution:
  def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
    # greedy algorithm on sorted array

    n = len(arr)
    arr.sort()

    if arr[0] != 1:
      arr[0] = 1

    for i in range(1, n):
      if abs(arr[i] - arr[i-1]) > 1:
        arr[i] = arr[i-1] + 1

    return arr[-1]

