class Solution:
  def averageWaitingTime(self, customers: List[List[int]]) -> float:
    # simulation
    
    n = len(customers)
    eta = 0
    wait_time = 0
    for t, p in customers:
      if eta > t:
        # current customer needs to wait
        eta += p
        wait_time += eta - t
      else:
        # chef is idle
        eta = t + p
        wait_time += p

    return wait_time / n

