class Solution:
  def largestOddNumber(self, num: str) -> str:
    # iteration

    n = len(num)
    for i in range(n-1, -1, -1):
      if ord(num[i]) % 2 == 1:
        return num[:i+1]
    
    return ""

