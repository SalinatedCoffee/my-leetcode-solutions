class Solution:
  def getWinner(self, arr: List[int], k: int) -> int:
    # simulation

    n = len(arr)
    if k >= n:
      return max(arr)
    
    a, b = 0, 1
    c_k = k
    while c_k:
      # left number wins, advance right number
      if arr[a] > arr[b]:
        b += 1
        c_k -= 1
      # right number wins, current right now left
      else:
        a = b
        b += 1
        c_k = k - 1
      a %= n
      b %= n

    return arr[a]

