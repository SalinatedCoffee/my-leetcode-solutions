class Solution:
  def arraySign(self, nums: List[int]) -> int:
    # iteration

    sign = True 
    for n in nums:
      if not n:
        return 0
      if n < 0:
        sign ^= True
    
    return 1 if sign else -1

