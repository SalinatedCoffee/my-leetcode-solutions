class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    # greedy with binary search on sorted list

    n = len(nums)
    # sort edge lengths in ascending order
    nums.sort()
    res = 0
    # for each pair of edges, search for smallest valid third edge using binary search
    for i in range(n - 1, -1, -1):
      for j in range(i):
        # search for index of smallest edge that would form a triangle with nums[l] and nums[h]
        t = nums[i] - nums[j]
        l = j + 1
        h = i - 1
        idx = -1
        while l <= h:
          m = l + (h - l) // 2
          if nums[m] > t:
            idx = m
            h = m - 1
          else:
            l = m + 1
        if idx != -1:
          # greedily increment counter by number of valid triangles that can be formed
          res += i - idx

    return res

