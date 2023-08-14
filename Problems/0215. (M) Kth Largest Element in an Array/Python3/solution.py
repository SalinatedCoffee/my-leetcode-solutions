class Solution:
  def findKthLargest(self, nums: List[int], k: int) -> int:
    # sorting

    nums.sort()

    return nums[-k]

