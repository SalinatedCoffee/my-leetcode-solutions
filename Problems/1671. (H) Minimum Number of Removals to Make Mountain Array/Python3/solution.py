class Solution:
  def minimumMountainRemovals(self, nums: List[int]) -> int:
    # longest increasing subsequence using binary search

    n = len(nums)

    # return list of length of LIS starting at each element of arr
    def lis(arr):
      lens = [0] * len(arr)
      cur_lis = [arr[0]]
      for i in range(1, len(arr)):
        # use binary search to find index of insertion
        idx = bisect_left(cur_lis, arr[i])
        if idx == len(cur_lis):
          cur_lis.append(arr[i])
        else:
          cur_lis[idx] = arr[i]
        lens[i] = len(cur_lis)
      
      return lens
    
    lis_lens = lis(nums)
    # reuse LIS algorithm to compute list of LDSes
    nums.reverse()
    lds_lens = lis(nums)
    lds_lens.reverse()

    # find optimal 'peak'
    res = float('inf')
    for i in range(n):
      if lis_lens[i] > 1 and lds_lens[i] > 1:
        res = min(res, n - lis_lens[i] - lds_lens[i] + 1)

    return res

