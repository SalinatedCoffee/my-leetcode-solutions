class Solution:
  def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
    # implied union-find on sorted array using dictionaries

    n = len(nums)
    # group swappable elements of nums
    nums_sorted = sorted(nums)
    cur = 0
    # value of v2g[i] is group number of i(with i being element in nums)
    v2g = {nums_sorted[0]: cur}
    # value of g2l[i] is deque of elements in group i
    g2l = defaultdict(deque)
    g2l[cur].append(nums_sorted[0])
    for i in range(1, n):
      if abs(nums_sorted[i-1] - nums_sorted[i]) > limit:
        cur += 1
      v2g[nums_sorted[i]] = cur
      g2l[cur].append(nums_sorted[i])

    # rearrange nums using groupings from previous step
    for i in range(n):
      cur = v2g[nums[i]]
      nums[i] = g2l[cur].popleft()

    return nums

