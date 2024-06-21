class Solution:
  def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
    # sliding window

    n = len(customers)
    # prepare window
    win_cur = 0
    for i in range(minutes):
      if grumpy[i]:
        win_cur += customers[i]
    # slide window over customers to find maximum number of satisfied customers
    win_max = win_cur
    for i in range(minutes, n):
      if grumpy[i-minutes]:
        win_cur -= customers[i-minutes]
      if grumpy[i]:
        win_cur += customers[i]
      win_max = max(win_max, win_cur)
    # compute number of satisfied customers when minutes is not used
    norm_sat = 0
    for i in range(n):
      if grumpy[i] == 0:
        norm_sat += customers[i]

    return norm_sat + win_max

