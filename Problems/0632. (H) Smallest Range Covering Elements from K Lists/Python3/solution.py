class Solution:
  def smallestRange(self, nums: List[List[int]]) -> List[int]:
    # merged sorted lists with sliding window

    # merge lists and sort
    mg_nums = []
    for i, row in enumerate(nums):
      mg_nums.extend(zip(row, [i]*len(row)))
    mg_nums.sort()

    n, k = len(mg_nums), len(nums)

    # freq[i] is number of elements from the i-th list within the current window
    freq = defaultdict(int)
    # l is index of left side of window
    # c is number of lists that have an element present in the current window
    l, c = 0, 0
    # current smallest valid range
    i, j = 0, float('inf')
    for r in range(n):
      freq[mg_nums[r][1]] += 1
      if freq[mg_nums[r][1]] == 1:
        c += 1
      # try incrementally contracting window while it is valid
      while c == k:
        cur = mg_nums[r][0] - mg_nums[l][0]
        # if range of window is smaller than previous, update
        if cur < j - i:
          i = mg_nums[l][0]
          j = mg_nums[r][0]
        freq[mg_nums[l][1]] -= 1
        if freq[mg_nums[l][1]] == 0:
          c -= 1
        l += 1

    return [i, j]

