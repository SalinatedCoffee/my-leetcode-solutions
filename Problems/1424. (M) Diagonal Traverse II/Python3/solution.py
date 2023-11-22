class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    # sort

    m = len(nums)
    # negate row number to sort in descending order
    vals = [[i+j, -i] for i in range(m) for j in range(len(nums[i]))]
    
    return [nums[-r][s+r] for s, r in sorted(vals)]

