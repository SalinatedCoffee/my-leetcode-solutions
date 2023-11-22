class Solution:
  def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    # brute force

    m = len(nums)
    n = max([len(i) for i in nums])

    ret = []
    for i in range(m):
      row, col = i, 0
      while row >= 0 and col <= n:
        if col < len(nums[row]):
          ret.append(nums[row][col])
        row -= 1
        col += 1

    for i in range(1, n):
      row, col = m-1, i
      while row >= 0 and col <= n:
        if col < len(nums[row]):
          ret.append(nums[row][col])
        row -= 1
        col += 1

    return ret

