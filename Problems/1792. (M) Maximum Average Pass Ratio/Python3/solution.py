class Solution:
  def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
    # greedy algorithm using max heap

    n = len(classes)
    # return the ratio gained by assigning an extra student to class
    # with x passing and y total students
    gain = lambda x, y: (x+1) / (y+1) - x / y
    # using max heap, sort by gainable ratio in descending order
    heap = [(-gain(p, t), p, t) for p, t in classes]
    heapify(heap)

    # assign students
    for _ in range(extraStudents):
      _, p, t = heappop(heap)
      heappush(heap, (-gain(p+1, t+1) , p+1, t+1))
    
    # compute average ratio
    avg_tot = 0
    while heap:
      _, p, t = heappop(heap)
      avg_tot += p / t

    return avg_tot / n

