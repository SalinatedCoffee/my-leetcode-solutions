class Solution:
  def construct(self, grid: List[List[int]]) -> 'Node':
    # recursion, recurse on quads if square is not uniform

    n = len(grid)

    def recurse(s_coord, size):
      y, x = s_coord
      total = 0
      # count number of 1s in square
      for i in range(y, y+size):
        total += sum(grid[i][x:x+size])
      # verify if square is leaf
      if total == size**2:
        return Node(1, True, None, None, None, None)
      elif not total:
        return Node(0, True, None, None, None, None)
      # get params for subsquares
      new_size = size // 2
      tl = recurse((y, x), new_size)
      tr = recurse((y, x+new_size), new_size)
      bl = recurse((y+new_size, x), new_size)
      br = recurse((y+new_size, x+new_size), new_size)
      return Node(-1, False, tl, tr, bl, br)

    return recurse((0, 0), n)

