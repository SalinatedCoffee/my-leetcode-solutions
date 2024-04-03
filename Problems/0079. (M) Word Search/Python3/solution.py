class Solution:
  def exist(self, board: List[List[str]], word: str) -> bool:
    # recursive DFS

    m, n = len(board), len(board[0])
    k = len(word)
    vec = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    # set of visited cells in current recursion branch
    self.visited = set()

    def recurse(i, j, idx = 1):
      # find word[idx:] in board starting at board[i][j]
      # base case, entire word matched
      if idx == k:
        return True
      self.visited.add((i, j))
      for dy, dx in vec:
        ny, nx = i + dy, j + dx
        # if neighboring cell exists, is not yet visited,
        # and contains the character word[idx], recurse on it
        if 0 <= ny < m and 0 <= nx < n and (ny, nx) not in self.visited \
          and board[ny][nx] == word[idx] and recurse(ny, nx, idx+1):
          return True
      self.visited.remove((i, j))
      
      return False

    # only start recursion if cell contains the character word[idx]
    for i in range(m):
      for j in range(n):
        if board[i][j] == word[0] and recurse(i, j):
          return True

    return False

