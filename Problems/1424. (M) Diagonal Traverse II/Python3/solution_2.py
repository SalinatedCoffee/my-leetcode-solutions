class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    # implicit sort

    m = len(nums)
    # rads[i] is a list of all elements in the i-th diagonal
    rads = defaultdict(list)
    for i in range(m-1, -1, -1):
      for j in range(len(nums[i])):
        rads[i+j].append(nums[i][j])
    
    ret = []
    r = 0
    while r in rads:
      ret.extend(rads[r])
      r += 1

    return ret

