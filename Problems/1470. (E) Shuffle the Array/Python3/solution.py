class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    # easier approach
    # copy items into new array

    res = [0] * (n*2)
    # first half
    for i in range(n):
      res[i*2] = nums[i]
    # second half
    for i in range(n, n*2):
      res[(i-n)*2+1] = nums[i]
    
    return res

