class Solution:
  def average(self, salary: List[int]) -> float:
    # iteration
    
    s_min, s_max, total = 10**6+1, 999, 0
    for s in salary:
      s_min = min(s_min, s)
      s_max = max(s_max, s)
      total += s
    
    return (total - s_min - s_max) / (len(salary) - 2)

