class Solution:
  def getRow(self, rowIndex: int) -> List[int]:
    # space-optimized dynamic programming

    prev = None
    for i in range(1, rowIndex+2):
      c_row = [1] * i
      for j in range(1, i-1):
        c_row[j] = prev[j-1] + prev[j]
      prev = c_row
    
    return prev

