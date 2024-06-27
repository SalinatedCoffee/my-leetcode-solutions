class Solution:
  def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    # backtracking

    ret = []
    cur = []

    def recurse(k, n, l = 1):
      # k is remaining number of selections
      # n is remaining value to sum to
      # l is the smallest available value
      
      # base case
      if k == 0:
        if n == 0:
          ret.append(cur[:])
        return
      
      for i in range(l, 10):
        cur.append(i)
        recurse(k-1, n-i, i+1)
        cur.pop()

    recurse(k, n)

    return ret

