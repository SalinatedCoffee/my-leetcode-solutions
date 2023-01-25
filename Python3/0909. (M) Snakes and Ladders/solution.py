from typing import List
from collections import deque

class Solution:
  def snakesAndLadders(self, board: List[List[int]]) -> int:
    # instinct is to use backtracking, but there is no criteria on when to backtrack
    # least number of moves, use BFS instead
    # how to handle cycles?
    self.n = len(board)
    self.last = self.n ** 2

    def get_square(square):
      square -= 1
      row = self.n - square // self.n - 1
      col = square % self.n
      if (square // self.n) % 2:
        col = self.n - col - 1
      print(square+1, row, col)

      return board[row][col]

    for i in range(1, self.last+1):
      get_square(i)
    #return 0
    
    visit = deque()
    visit.append((1,0))
    ret = []
    while len(visit):
      cur, moves = visit.popleft()
      print(f'At sq. {cur} with {moves} moves')
      if cur == self.last:
        ret.append(moves)
        continue
      if cur > self.last:
        continue
      val = get_square(cur)
      if val != -1:
        print(f'snake/ladder, move to {val}')
        cur = val
      for i in range(1, 7):
        visit.append((cur+i,moves+1))

    return min(ret) if ret else -1

obj = Solution()
b1 = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
b2 = [[-1,-1,-1],[-1,9,8],[-1,8,9]]
ret = obj.snakesAndLadders(b2)
print(ret)
