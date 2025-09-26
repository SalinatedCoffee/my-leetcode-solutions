class Solution:
  def triangleNumber(self, nums: List[int]) -> int:
    # greedy algorithm on sorted list

    # sort edge lengths in ascending order
    nums.sort()
    n = len(nums)
    res = 0
    # for each pair of edges, walk rest of list to count number of valid third edges
    for i in range(n-2):
      k = i + 2
      for j in range(i+1, n-1):
        while k < n and nums[i] + nums[j] > nums[k]:
          k += 1
        # increment counter accordingly
        res += k - j - 1

    return res

