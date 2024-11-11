class Solution:
  def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
    # bit manipulation with sliding window

    # given a list of binary digits arr, concatenate the bits
    # and return the resulting integer
    def bitarray_to_integer(arr):
      res = 0
      for i in range(len(arr)-1, -1, -1):
        if arr[i]:
          res |= 1
        res <<= 1

      return res >> 1
    
    # update the contents of binary digit array arr using the binary representation of val
    # increment counters if add is True, decrement otherwise
    def update_bitarray(arr, val, add=True):
      for i in range(len(arr)):
        if val & 1:
          arr[i] += 1 if add else -1
        val >>= 1

    n = len(nums)
    res = float('inf')
    l, h = 0, 0
    bits = [0] * 32
    while h < n:
      update_bitarray(bits, nums[h])
      while l <= h and bitarray_to_integer(bits) >= k:
        res = min(res, h - l + 1)
        update_bitarray(bits, nums[l], False)
        l += 1
      h += 1

    return res if res != float('inf') else -1

