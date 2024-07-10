class Solution:
  def solveSudoku(self, board: List[List[str]]) -> None:
    # backtracking using sets with no heuristic

    # initialize available values for each row, column, and subgrid,
    # and find all empty squares
    sudoku_set = lambda: set(str(i) for i in range(1, 10))
    row = [sudoku_set() for _ in range(9)]
    col = [sudoku_set() for _ in range(9)]
    sub = [[sudoku_set() for _ in range(3)] for _ in range(3)]
    empty = []
    for i in range(9):
      for j in range(9):
        if board[i][j] != '.':
          row[i].remove(board[i][j])
          col[j].remove(board[i][j])
          sub[i//3][j//3].remove(board[i][j])
        else:
          empty.append((i, j))
    
    def recurse(i):
      # return True if a solution is found starting at the i-th empty square
      if i == len(empty):
        return True
      
      r, c = empty[i]
      for v in row[r] & col[c] & sub[r//3][c//3]:
        board[r][c] = v
        row[r].remove(v)
        col[c].remove(v)
        sub[r//3][c//3].remove(v)
        if recurse(i+1):
          return True
        row[r].add(v)
        col[c].add(v)
        sub[r//3][c//3].add(v)
      board[r][c] = '.'

      return False
    
    recurse(0)

