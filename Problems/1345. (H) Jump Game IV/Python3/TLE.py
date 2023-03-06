class Solution:
  def minJumps(self, arr: List[int]) -> int:
    # bfs, use dictonary mapping value to indices

    v2i = {}
    for i, n in enumerate(arr):
      if n not in v2i:
        v2i[n] = []
      v2i[n].append(i)
    
    nodes = deque()
    visited = set()
    nodes.append((0, 0))
    while nodes:
      idx, jmp = nodes.popleft()
      if idx in visited:
        continue
      visited.add(idx)
      if idx == len(arr)-1:
        return jmp
      # consider furthest index first
      for i in reversed(v2i[arr[idx]]):
        nodes.append((i, jmp+1))
      # add prev/next elements if available
      if idx:
        nodes.append((idx-1, jmp+1))
      nodes.append((idx+1, jmp+1))
    
    return -1

