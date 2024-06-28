class Solution:
  def totalNQueens(self, n: int) -> int:
    # backtracking
    
    self.ret = 0
    # occupied columns
    self.cols = [False] * n
    # coordinates of previously placed queens
    self.prev = set()

    def recurse(rem):
      # all queens placed
      if rem == 0:
        self.ret += 1
        return
      # get current row
      row = n - rem
      # try all possible placements on current row
      for i in range(n):
        # column is occupied
        if self.cols[i]:
          continue
        flag = False
        for r, c in self.prev:
          # current square is on diagonal of previously placed queen
          if abs(r - row) == abs(c - i):
            flag = True
            break
        # current square is valid
        if not flag:
          self.cols[i] = True
          self.prev.add((row, i))
          recurse(rem - 1)
          self.cols[i] = False
          self.prev.remove((row, i))
    
    recurse(n)

    return self.ret

