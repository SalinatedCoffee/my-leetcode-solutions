class Solution:
  def maximumOddBinaryNumber(self, s: str) -> str:
    # brute force
    
    pop = 0
    for c in s:
      if c == '1':
        pop += 1

    return '1'*(pop-1) + '0'*(len(s)-pop) + '1'

