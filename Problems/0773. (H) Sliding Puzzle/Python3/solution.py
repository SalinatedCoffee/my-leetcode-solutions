class Solution:
  def slidingPuzzle(self, board: List[List[int]]) -> int:
    # iterative BFS

    # moves[i] is list of indices of characters that can be swapped when 0 has index i
    moves = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]

    # given the string represenation of current board, index of 0, and index of char to swap with
    # swap the characters and return the modified string
    def move(board, zero, target):
      board = list(board)
      board[zero], board[target] = board[target], board[zero]
      return "".join(board)
    
    goal = "123450"
    root = "".join([str(i) for row in board for i in row])
    visited = set([root])
    nodes = deque([(root, 0)])
    # run BFS
    while nodes:
      cur, d = nodes.popleft()
      if cur == goal:
        return d
      zero = cur.index('0')
      # explore possible move if the resulting board configuration has not yet been seen
      for nxt_pos in moves[zero]:
        nxt = move(cur, zero, nxt_pos)
        if nxt not in visited:
          visited.add(nxt)
          nodes.append((nxt, d + 1))

    return -1

