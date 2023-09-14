class Solution:
  def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    # recursive DFS

    self.n = len(tickets)
    tick = 0
    adj = defaultdict(list)
    for o, d in tickets:
      adj[o].append((d, tick))
      tick += 1
    for l in adj.values():
      l.sort(key=lambda x: x[0])
    self.dfs("JFK", set(), itinerary := ["JFK"], adj)

    return itinerary
  
  def dfs(self, cur, visited, itinerary, adj):
    if len(visited) == self.n:
      return True
    for dest in adj[cur]:
      if dest not in visited:
        visited.add(dest)
        itinerary.append(dest[0])
        if self.dfs(dest[0], visited, itinerary, adj):
          return True
        visited.remove(dest)
        itinerary.pop()

