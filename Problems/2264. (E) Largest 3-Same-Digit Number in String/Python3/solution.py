class Solution:
  def largestGoodInteger(self, num: str) -> str:
    # simple iteration
    
    n = len(num)
    run, d = 1, ""
    for i in range(1, n):
      if num[i-1] == num[i]:
        run += 1
      else:
        run = 1
      if run == 3:
        d = max(d, num[i-1])
    
    return d*3

