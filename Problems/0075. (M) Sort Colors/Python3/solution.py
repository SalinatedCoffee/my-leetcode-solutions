class Solution:
  def sortColors(self, nums: List[int]) -> None:
    # two pass counting sort

    n = len(nums)
    # generate frequency count of colors
    freq = [0, 0, 0]
    for num in nums:
      freq[num] += 1
    
    # overwrite nums
    for i in range(n):
      for c in [0, 1, 2]:
        if freq[c]:
          nums[i] = c
          freq[c] -= 1
          break

