class Solution:
  def solveNQueens(self, n: int) -> List[List[str]]:
    # backtracking

    ret = []
    # current state of board
    board = [['.']*n for _ in range(n)]
    # list of coordinates of queens currently on the board
    placed = []
    # col_avail[i] is True if a queen is not placed on the i-th column
    col_avail = [True]*n

    def recurse(row):
      # search all valid queen placements starting at row row
      # using board, placed, and col_avail

      # all queens placed
      if row == n:
        ret.append([''.join(b_row) for b_row in board])
        return
      # for each column in current row
      for col in range(n):
        # column is already occupied
        if col_avail[col] is False:
          continue
        # check if current square is on a diagonal to any queens on the board
        valid = True
        for r, c in placed:
          if abs(r - row) == abs(c - col):
            valid = False
            break
        # queen can be placed on current square
        if valid:
          board[row][col] = 'Q'
          placed.append((row, col))
          col_avail[col] = False
          recurse(row+1)
          board[row][col] = '.'
          placed.remove((row, col))
          col_avail[col] = True
    
    recurse(0)

    return ret

