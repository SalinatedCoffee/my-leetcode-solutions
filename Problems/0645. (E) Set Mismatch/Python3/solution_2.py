class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    # math (sum of sequences)

    n = len(nums)
    diff = n * (n + 1) // 2
    diff_sq = n * (n + 1) * (2*n + 1) // 6
    for num in nums:
      diff -= num
      diff_sq -= num ** 2
    dupe = (diff_sq - diff ** 2) // (2 * diff)

    return [dupe, dupe + diff]

