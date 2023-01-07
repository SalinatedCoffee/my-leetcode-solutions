class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # start from beginning of list
    # iterate while computing total fuel and cost up to that point
    balance = 0
    total = 0
    latest_start = 0
    for i in range(len(gas)):
      total += gas[i] - cost[i]
      balance += gas[i] - cost[i]
      # if fuel in tank goes below zero
      if balance < 0:
        # abandon previous stations
        balance = 0
        # set new interval index
        latest_start = i + 1
  
    # if total fuel - cost is not negative, a solution exists
    if total >= 0:
      return latest_start
    return -1

