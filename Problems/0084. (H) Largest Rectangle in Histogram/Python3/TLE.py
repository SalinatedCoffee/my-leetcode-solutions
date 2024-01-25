class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    # brute force
    
    n = len(heights)

    ret = 0
    for i in range(n):
      min_height = heights[i]
      for j in range(i, -1, -1):
        min_height = min(min_height, heights[j])
        ret = max(ret, min_height * (i - j + 1))

    return ret

