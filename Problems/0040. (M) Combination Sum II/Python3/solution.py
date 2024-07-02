class Solution:
  def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    # backtracking on keys of dictionary

    c_freq = Counter(candidates)
    keys = list(c_freq.keys())
    k = len(keys)
    self.ret, self.cur = [], []
    def recurse(i, r):
      # find combination of keys[i:] that adds up to r

      # base case, exit if no keys remaining or r is 0
      if i == k or r == 0:
        # only add current combination if r is 0
        if r == 0:
          self.ret.append(self.cur[:])
        return

      # try using incrementally more of current value
      count = 0
      while count <= c_freq[keys[i]] and r >= 0:
        recurse(i+1, r)
        self.cur.append(keys[i])
        r -= keys[i]
        count += 1
      # revert combination to original state
      self.cur = self.cur[:-count]

    recurse(0, target)

    return self.ret

