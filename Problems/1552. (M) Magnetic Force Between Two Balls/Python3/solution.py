class Solution:
  def maxDistance(self, position: List[int], m: int) -> int:
    # binary search on sorted list using greedy algorithm

    n = len(position)
    position.sort()
    # set initial search space
    l, h = 1, position[-1] // (m-1)
    ret = 0
    while l <= h:
      mid = l + (h - l) // 2
      # validate midpoint by greedily placing ball in buckets
      placed = 1
      prev = position[0]
      idx = 1
      while idx < n:
        if position[idx] - prev >= mid:
          prev = position[idx]
          placed += 1
        idx += 1
      # if midpoint valid, a larger value may also be valid
      if placed >= m:
        l = mid + 1
        ret = mid
      else:
        h = mid - 1

    return ret

