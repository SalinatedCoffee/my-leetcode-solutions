class Solution:
  def getHappyString(self, n: int, k: int) -> str:
    # backtracking

    self.res = ""
    self.cur = ""
    self.idx = 0
    self.recurse(n, k)

    return self.res
  
  def recurse(self, n, k):
    # generate happy strings of length n in ascending lexicographical order
    if len(self.cur) == n:
      self.idx += 1
      if self.idx == k:
        self.res = self.cur
      return

    for c in "abc":
      if len(self.cur) and self.cur[-1] == c:
        continue
      self.cur += c
      self.recurse(n, k)
      # stop recursion if result was found
      if self.res:
        return
      self.cur = self.cur[:-1]

