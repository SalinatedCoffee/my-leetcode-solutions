class Solution:
  def partition(self, s: str) -> List[List[str]]:
    # palindromes may have odd or even length
    # start from idx 0, try even and odd palin recursively

    self.ret = []
    self.cur = []
    def recurse(start, end):
      c_start, c_end = start, end
      # if oob
      if end >= len(s):
        # entire string consumed if called with same start and end
        if start == end:
          # add current partitioning to return list
          self.ret.append(self.cur[:])
        return
      # verify if substring s[start:end+1] is palindrome
      while c_end >= c_start:
        # exit early if not
        if s[c_start] != s[c_end]:
          return
        c_start += 1
        c_end -= 1
      # current substring is palindrome, add to temp partitioning
      self.cur.append(s[start:end+1])
      # try all substrings starting at index end+1
      for i in range(end+1, len(s)+1):
        recurse(end+1, i)
      # remove current partition from temp before exiting
      self.cur.pop()
      return
    
    for i in range(len(s)):
      recurse(0, i)
     
    return self.ret

