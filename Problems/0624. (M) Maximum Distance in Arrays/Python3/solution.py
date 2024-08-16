class Solution:
  def maxDistance(self, arrays: List[List[int]]) -> int:
    # greedy algorithm with heaps

    arr_min = [(-10**4, -1)]*2
    arr_max = [(-10**4, -1)]*2
    for i, arr in enumerate(arrays):
      heappush(arr_min, (-arr[0], i))
      heappop(arr_min)
      heappush(arr_max, (arr[-1], i))
      heappop(arr_max)

    min_b = heappop(arr_min)
    min_a = heappop(arr_min)
    max_b = heappop(arr_max)
    max_a = heappop(arr_max)

    ret = -1
    if min_a[1] == max_a[1]:
      ret = max(max_b[0] + min_a[0], max_a[0] + min_b[0])
    else:
      ret = max_a[0] + min_a[0]

    return ret

