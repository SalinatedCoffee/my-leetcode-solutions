class Solution:
  def minimumDeviation(self, nums: List[int]) -> int:
    # max heap based approach

    ascd = []
    min_val = 10**9+1
    # add all values in max heap, multiply if odd
    for i in nums:
      n = 2*i if i % 2 else i
      heappush(ascd, -n)
      min_val = min(min_val, n)

    min_diff = 10**9+1
    # while largest value is even
    while not ascd[0] % 2:
      min_diff = min(min_diff, -ascd[0] - min_val)
      min_val = min(min_val, -ascd[0] // 2)
      heappush(ascd, ascd[0] // 2)
      heappop(ascd)

    return min(min_diff, -ascd[0] - min_val)

