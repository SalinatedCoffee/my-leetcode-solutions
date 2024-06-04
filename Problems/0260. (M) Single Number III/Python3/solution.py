class Solution:
  def singleNumber(self, nums: List[int]) -> List[int]:
    # XOR sums

    # compute XOR sum of all elements
    xor_all = reduce(lambda x, y: x ^ y, nums)
    # arbitrarily find raised bit in XOR sum
    mask = 1
    while xor_all & mask == 0:
      mask <<= 1
    # compute XOR sum of all elements with a bit raised in the same position
    xor_a = 0
    for num in nums:
      if num & mask:
        xor_a ^= num

    return [xor_a, xor_a ^ xor_all]

