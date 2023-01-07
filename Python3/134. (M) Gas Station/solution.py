class Solution:
  def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
    # easy but inefficient solution is to just try every index
    # n^2 worst case
    # modulo arithmetic for wraparound

    stations = len(gas)
    for i in range(stations):
      tank = 0
      dne = False
      # start at station i, wrap around at end of station list
      for j in [(i+x)%stations for x in range(stations)]:
        tank += gas[j]
        if tank < cost[j]:
          dne = True
          break
        tank -= cost[j]
      # loop exited prematurely, run not possible at station i
      if not dne:
        return i
  
    return -1

