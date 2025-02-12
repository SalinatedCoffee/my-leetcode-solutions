class Solution:
  def maximumSum(self, nums: List[int]) -> int:
    # dictionary with max heaps

    # digit_sum[i] is max heap of elements with digit sum i
    digit_sum = defaultdict(list)
    for num in nums:
      d, temp = 0, -num
      while num:
        d += num % 10
        num //= 10
      heappush(digit_sum[d], temp)
    
    # search all groups for largest sum
    res = -1
    for v in digit_sum.values():
      if len(v) < 2:
        continue
      res = max(res, -(heappop(v)+heappop(v)))

    return res

