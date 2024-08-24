class Solution:
  def smallestDistancePair(self, nums: List[int], k: int) -> int:
    # binary search with dynamic programming

    n = len(nums)
    nums.sort()

    max_d = nums[-1]*2
    # pre[i] is number of values in nums less than or equal to i
    pre = [0] * max_d
    # val[i] is number of values in nums equal to i
    val = defaultdict(int)

    # return number of pairs in nums with distance less than or equal to d
    def count(d):
      c, i = 0, 0
      while i < n:
        cur = nums[i]
        cur_cnt = val[cur]
        # get number of viable elements with value greater than cur
        gt = pre[min(cur + d, len(pre) - 1)] - pre[cur]
        # get number of pairs of elements with value cur
        eq = cur_cnt * (cur_cnt - 1) // 2
        # compute number of viable pairs and update total count
        c += gt * cur_cnt + eq
        while i + 1 < n and nums[i] == nums[i+1]:
          i += 1
        i += 1

      return c

    # populate pre and val
    idx = 0
    for i in range(max_d):
      while idx < n and nums[idx] <= i:
        idx += 1
      pre[i] = idx
    for i in range(n):
      val[nums[i]] += 1

    # binary search on distance
    l, h = 0, nums[-1] - nums[0]
    while l < h:
      m = l + (h - l) // 2
      cnt = count(m)
      if cnt < k:
        l = m + 1
      else:
        h = m

    return l

