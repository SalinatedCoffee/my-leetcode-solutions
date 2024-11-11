class Solution:
  def primeSubOperation(self, nums: List[int]) -> bool:
    # greedy algorithm

    # generate list of primes from 2 to n
    def list_primes(n):
      vals = [True] * (n+1)
      vals[1] = False
      for i in range(2, int(sqrt(n+1))+1):
        if vals[i] is True:
          for j in range(i**2, n+1, i):
            vals[j] = False

      return vals

    # primes[i] is True if i is prime, False otherwise
    primes = list_primes(max(nums))
    # target value for current element of nums
    cur = 1
    idx = 0
    while idx < len(nums):
      d = nums[idx] - cur
      # current element is smaller than target
      if d < 0:
        return False
      # can subtract prime from current element to achieve target
      if primes[d] is True or d == 0:
        idx += 1
        cur += 1
      # increment target by 1 and try again
      else:
        cur += 1

    return True

