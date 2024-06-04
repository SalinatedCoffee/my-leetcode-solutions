class Solution:
  def countTriplets(self, arr: List[int]) -> int:
    # prefix sums

    n = len(arr)
    # precompute prefix XOR sums
    prefix = [0] * (n+1)
    for i in range(1, n+1):
      prefix[i] = prefix[i-1] ^ arr[i-1]
    
    ret = 0
    # count number of possible triplets for all pairs of i and k
    for i in range(n+1):
      for j in range(i+1, n+1):
        # i and k is a valid pair
        if prefix[i] == prefix[j]:
          ret += j - i - 1

    return ret

