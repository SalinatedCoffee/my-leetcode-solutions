class Solution:
  def zeroFilledSubarray(self, nums: List[int]) -> int:
    # iterate while counting zeros

    run = 0
    ret = 0

    for n in nums:
      if n == 0:
        run += 1
      elif run:
        # Gaussian sum
        ret += run * (run+1) // 2
        run = 0
    
    # count last run of zeros
    return ret if not run else ret + run * (run+1) // 2
       
