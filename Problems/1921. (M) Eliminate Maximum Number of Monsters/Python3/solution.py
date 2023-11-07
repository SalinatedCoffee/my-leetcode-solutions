class Solution:
  def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
    # greedy on sorted list

    n = len(dist)
    t_time = [ceil(d/s) for d, s in zip(dist, speed)]
    t_time.sort()
    k = 1
    t_rem = t_time[0]
    for i in range(1, n):
      t_rem += t_time[i] - t_time[i-1]
      t_rem -= 1
      if t_rem == 0:
        return k
      k += 1

    return k

