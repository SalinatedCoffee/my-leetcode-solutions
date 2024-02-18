class Solution:
  def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
    # greedy algorithm on heap

    n = len(heights)
    heap = []
    for i in range(1, n):
      diff = heights[i] - heights[i-1]
      if diff > 0:
        heappush(heap, diff)
        # prioritize using ladders first
        if ladders:
          ladders -= 1
        # if no ladders available, change history and brick shortest climb
        elif heap[0] <= bricks:
          bricks -= heappop(heap)
        else:
          return i-1

    return n-1

