class Solution:
  def largestRectangleArea(self, heights: List[int]) -> int:
    # monotonic stack

    n = len(heights)

    def first_smaller(left = True):
      # return list of first item smaller than i on its left/right for all i
      ret = [-1] * n if left else [n] * n
      params = [n] if left else [n-1, -1, -1]
      stack = []
      for i in range(*params):
        while stack and heights[stack[-1]] >= heights[i]:
          if left is False and heights[stack[-1]] == heights[i]:
            break
          stack.pop()
        if stack:
          ret[i] = stack[-1]
        stack.append(i)

      return ret

    left, right = first_smaller(), first_smaller(False)
    ret = 0
    for i in range(n):
      # compute maximum area at each index
      ret = max(ret, (right[i] - left[i] - 1) * heights[i])

    return ret

