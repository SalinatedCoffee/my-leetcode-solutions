class Solution:
  def frequencySort(self, nums: List[int]) -> List[int]:
    # sort list using values from dictionary

    freq = Counter(nums)
    return sorted(nums, key=lambda x: (freq[x], -x))

