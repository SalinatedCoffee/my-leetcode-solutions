class Solution:
  def findTheWinner(self, n: int, k: int) -> int:
    # recursion

    def recurse(n, k):
      # return index of winning player among n players skipping k people
      if n == 1:
        return 0
      return (recurse(n-1, k) + k) % n

    return recurse(n, k) + 1

