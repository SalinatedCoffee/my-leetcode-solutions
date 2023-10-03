class Solution:
  def winnerOfGame(self, colors: str) -> bool:
    # compute number of moves

    n = len(colors)
    # sanity check
    if n < 3:
      return False

    idx = 0
    moves_a, moves_b = 0, 0
    for i in range(1, n):
      if colors[i] != colors[i-1]:
        moves = i - idx - 2
        idx = i
        if moves <= 0:
          continue
        if colors[i-1] == 'A':
          moves_a += moves
        else:
          moves_b += moves
    # process last run of colors
    moves = n - idx - 2
    if moves > 0:
      if colors[-1] == 'A':
        moves_a += moves
      else:
        moves_b += moves

    return moves_a > moves_b

