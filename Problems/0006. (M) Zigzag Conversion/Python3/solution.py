class Solution:
  def convert(self, s: str, numRows: int) -> str:
    # simulate traversing s in zigzag layout
    # explicitly construct each row and concatenate after

    # sanity check
    if numRows == 1:
      return s

    # initialize rows
    rows = [""] * numRows
    backward = True
    index = 0
    for c in s:
      rows[index] += c
      # reverse row direction at first or last row
      if index == 0 or index == numRows - 1:
        backward = not backward
      # iterate through rows accordingly
      if backward:
        index -= 1
      else:
        index += 1

    return "".join(rows)

