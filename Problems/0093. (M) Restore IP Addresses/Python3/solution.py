class Solution:
  def restoreIpAddresses(self, s: str) -> List[str]:
    # backtracking, prune early if current substring is invalid ip

    # sanity check
    if len(s) > 12:
      return []
    
    def validate(i, j):
      # first digit is 0
      if s[i] == '0':
        # substring length is not 1
        if j-i > 0:
          return False
      # substring is larger than 255
      elif int(s[i:j+1]) > 255:
        return False
      return True
    
    self.ret = []
    self.cur = []
    def recurse(start):
      # oob and 4 numbers validated
      if start >= len(s) and len(self.cur) == 4:
        self.ret.append('.'.join(self.cur))
        return
      # try possible substrings from current, recurse if valid
      for i in range(start, min(len(s), start+3)):
        if validate(start, i):
          self.cur.append(s[start:i+1])
          recurse(i+1)
          self.cur.pop()
    
    recurse(0)
    
    return self.ret

