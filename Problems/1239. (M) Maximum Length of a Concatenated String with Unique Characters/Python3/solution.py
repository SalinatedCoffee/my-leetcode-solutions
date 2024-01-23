class Solution:
  def maxLength(self, arr: List[str]) -> int:
    # top-down dynamic programming (memoization)

    n = len(arr)

    @cache
    def recurse(i, b):
      # returns longest length of concatenated string using strings in arr[i-1:]
      # where b set of unique letters have already been used
      if i == n:
        return 0
      b_n = 0
      for c in arr[i]:
        bit = 1 << (ord(c) - ord('a'))
        # check if current string contains only unique letters
        if b_n & bit:
          return recurse(i+1, b)
        b_n += bit
      b_temp, b_n_temp = b, b_n
      while b_temp and b_n_temp:
        # check if current string contains only available letters
        if b_temp & 1 and b_n_temp & 1:
          return recurse(i+1, b)
        b_temp >>= 1
        b_n_temp >>= 1

      return max(recurse(i+1, b), len(arr[i]) + recurse(i+1, b + b_n))

    return recurse(0, 0)

