class Solution:
  def shuffle(self, nums: List[int], n: int) -> List[int]:
    # in-place solution using bit manip.

    # bitmask for lower 10 bits
    mask_lower = 2**10-1

    # collapse upper half into lower half
    for i in range(n, 2*n):
      n2 = nums[i] << 10
      nums[i-n] |= n2
    
    # expand lower half into correct positions in reverse order
    for i in range(n-1, -1, -1):
      n2 = nums[i] >> 10
      n1 = nums[i] & mask_lower
      nums[2*i+1] = n2
      nums[2*i] = n1
    
    return nums

