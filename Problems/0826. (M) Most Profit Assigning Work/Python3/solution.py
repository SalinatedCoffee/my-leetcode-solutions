class Solution:
  def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
    # greedy algorithm on sorted lists

    n, m = len(difficulty), len(worker)
    # sort jobs by profit in descending order
    jobs = list(sorted(zip(profit, difficulty), reverse=True))
    # sort workers by ability in ascending order
    worker.sort()
    ret = 0
    l = m
    # starting with the highest paying job...
    for j_prof, j_diff in jobs:
      # ...greedily assign it to as many workers as possible
      idx = bisect_left(worker, j_diff)
      # if job is unassignable, skip to next job
      if idx < l:
        ret += j_prof * (l - idx)
        l = idx
      # if all workers have been assigned a job, stop early
      if idx == 0:
        return ret

    return ret

