class Solution:
  def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
    # heaps with sorted list

    n = len(times)
    # sort times in ascending order of start time while preserving index of each element
    times = list(enumerate(times))
    times.sort(key=lambda x: x[1][0])
    # min heap of currently vacent chairs, sorted by label
    vacent = [i for i in range(n)]
    heapify(vacent)
    # min heap of currently occupied chairs, sorted by end time of occupation
    occupied = []
    for i in range(n):
      cur, end = times[i][1]
      # evict vacent chairs
      while occupied and occupied[0][0] <= cur:
        _, newly_vacent = heappop(occupied)
        heappush(vacent, newly_vacent)
      # retrieve vacent chair to seat the current person
      cur_seat = heappop(vacent)
      # current person is target
      if times[i][0] == targetFriend:
        return cur_seat
      # mark chair as occupied
      heappush(occupied, (end, cur_seat))

    # this line is unreachable given problem constraints
    return -1

