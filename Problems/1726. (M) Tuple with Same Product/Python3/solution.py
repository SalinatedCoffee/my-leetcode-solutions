class Solution:
  def tupleSameProduct(self, nums: List[int]) -> int:
    # frequency of pair products using dictionary

    n = len(nums)
    prods = defaultdict(int)
    res = 0
    # compute and count products for all possible element pairs
    for i in range(n):
      for j in range(i+1, n):
        prods[nums[i] * nums[j]] += 1

    # count permutations
    for v in prods.values():
      pairs = (v - 1) * v // 2
      res += 8 * pairs

    return res

