class Solution:
  def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
    # recursive BFS, do computation on return value of recursive call?

    # sanity check
    if not roads:
      return 0

    # generate adjacency list
    adj = [[] for _ in range(len(roads)+1)]
    for u, v in roads:
      adj[u].append(v)
      adj[v].append(u)

    visited = [0] * len(adj)

    def recurse(node):
      if visited[node]:
        return 0
      nonlocal fuel
      visited[node] = 1
      reps = 1
      for i in adj[node]:
        sub_reps = recurse(i)
        # compute number of cars for one subtree
        sub_cars = sub_reps // seats
        sub_cars += 1 if sub_reps % seats else 0
        fuel += sub_cars
        reps += sub_reps
      return reps

    fuel = 0
    recurse(0)
    return fuel

