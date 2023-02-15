class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    # iterative one liner approach
    return (nums[j] for i in range(n) for j in [i, i+n])

