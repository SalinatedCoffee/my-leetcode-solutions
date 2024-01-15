class Solution:
  def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    # dynamic programming on sorted list with binary search
    
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))

    @cache
    def recurse(idx):
      # return maximum profit of scheduling jobs ini sorted jobs[idx:]
      if idx >= n:
        return 0
      n_idx = bisect_left(jobs, jobs[idx][1], key=lambda x: x[0])

      return max(recurse(idx+1), jobs[idx][2] + recurse(n_idx))
    
    return recurse(0)

