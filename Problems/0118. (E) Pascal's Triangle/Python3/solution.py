class Solution:
  def generate(self, numRows: int) -> List[List[int]]:
    # dynamic programming
    
    ret = []
    for i in range(1, numRows+1):
      c_row = [1] * i
      for j in range(1, i-1):
        c_row[j] = ret[-1][j-1] + ret[-1][j]
      ret.append(c_row)
    
    return ret

