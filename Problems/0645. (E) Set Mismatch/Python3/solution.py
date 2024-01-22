class Solution:
  def findErrorNums(self, nums: List[int]) -> List[int]:
    # brute force

    freq = [0] * len(nums)
    for num in nums:
      freq[num-1] += 1

    ret = [-1, -1]
    for i in range(len(nums)):
      if freq[i] == 0:
        ret[1] = i + 1
      elif freq[i] == 2:
        ret[0] = i + 1

    return ret

