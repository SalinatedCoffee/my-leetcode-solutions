class Solution:
  def threeConsecutiveOdds(self, arr: List[int]) -> bool:
    # sliding window

    n = len(arr)
    # sanity check
    if n < 3:
      return False

    # number of odd values in current window
    cur = 0
    for i in range(n):
      cur += arr[i] % 2
      if i > 2:
        cur -= arr[i-3] % 2
      if cur == 3:
        return True

    return False

