class Solution:
  # backtracking

  def letterCombinations(self, digits: str) -> List[str]:
    self.mappings = ["", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
    self.ret = []
    self.recurse(digits, "")

    return self.ret
  
  def recurse(self, digits, sel):
    if not digits:
      if sel:
        self.ret.append(sel)
    else:
      idx = ord(digits[0]) - ord('0')
      for c in self.mappings[idx]:
        self.recurse(digits[1:], sel+c)

