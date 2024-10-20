class Solution:
  def findKthBit(self, n: int, k: int) -> str:
    # recursion

    if n == 1:
      return '0'
    
    l = 1 << n
    if k > l // 2:
      return '0' if self.findKthBit(n-1, l-k) != '0' else '1'
    elif k == l // 2:
      return '1'

    return self.findKthBit(n-1, k)

