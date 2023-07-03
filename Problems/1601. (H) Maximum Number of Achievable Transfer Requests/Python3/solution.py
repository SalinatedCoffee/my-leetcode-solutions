class Solution:
  def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
    # backtracking

    req_n = len(requests)
    self.ret = -1
    deltas = [0] * n

    def recurse(i, r):
      if i == req_n:
        for d in deltas:
          if d:
            return
        self.ret = max(self.ret, r)
        return
      u, v = requests[i]
      deltas[u] -= 1
      deltas[v] += 1
      recurse(i+1, r+1)
      deltas[u] += 1
      deltas[v] -= 1
      recurse(i+1, r)

    recurse(0, 0)

    return self.ret
    
