class Solution:
  def numIdenticalPairs(self, nums: List[int]) -> int:
    # hashing

    # i2i[n] is number of occurences of integer n in nums
    i2i = Counter(nums)

    return sum([n*(n-1)//2 for n in i2i.values()])

