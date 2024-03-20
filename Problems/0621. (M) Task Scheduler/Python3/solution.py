class Solution:
  def leastInterval(self, tasks: List[str], n: int) -> int:
    # greedy algorithm on max heap

    ret = 0
    # count frequency of each unique task
    freq = [0] * 26
    for task in tasks:
      freq[ord(task) - ord('A')] -= 1
    # convert frequency counts into max heap
    heapify(freq := [x for x in freq if x])
    while freq:
      cycle = n + 1
      jobs = []
      jobs_count = 0
      # simulate one cycle
      while cycle and freq:
        v = heappop(freq)
        cycle -= 1
        if -v > 1:
          jobs.append(v+1)
        jobs_count += 1
      # update frequencies in max heap
      for job in jobs:
        heappush(freq, job)
      # count elapsed time
      ret += jobs_count if not freq else n + 1

    return ret

