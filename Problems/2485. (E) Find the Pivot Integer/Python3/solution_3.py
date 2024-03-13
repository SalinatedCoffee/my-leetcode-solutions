class Solution:
  def pivotInteger(self, n: int) -> int:
    # math

    x = sqrt((n*n+n)/2)
    
    return -1 if x % 1 else int(x)

