class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    # instinct is to use backtracking, but we don't know when to backtrack
    # least number of moves, use BFS instead
    self.n = len(board)
    self.last = self.n ** 2

    # translate square to indices in board
    def get_square(square):
      square -= 1
      row = self.n - square // self.n - 1
      col = square % self.n
      if (square // self.n) % 2:
        col = self.n - col - 1

      return board[row][col]
    
    # 'flatten' board into 1D list
    board_f = [-1]
    for i in range(1, self.last+1):
      board_f.append(get_square(i))
   
    visit = deque()
    visit.append((1,0))
    seen = set()
    while len(visit):
      cur, moves = visit.popleft()
      # reached destination
      if cur == self.last:
        return moves
      # check if already visited
      if cur in seen:
        continue
      else:
        seen.add(cur)
      for i in range(cur+1, min(cur+6, self.last)+1):
        # check if next has snake or ladder
        if board_f[i] != -1:
          nxt = board_f[i]
        else:
          nxt = i
        visit.append((nxt,moves+1))

    return -1

