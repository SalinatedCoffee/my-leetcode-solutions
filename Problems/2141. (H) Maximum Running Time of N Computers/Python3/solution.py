class Solution:
  def maxRunTime(self, n: int, batteries: List[int]) -> int:
    # prefix sum on sorted array

    batt_sorted = sorted(batteries)
    live = batt_sorted[-n:]
    extra = sum(batt_sorted[:-n])
    for i in range(n-1):
      if extra < (i+1) * (live[i+1] - live[i]):
        return live[i] + extra // (i+1)
      extra -= (i+1) * (live[i+1] - live[i])
    
    return live[-1] + extra // n

