class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    # greedy algorithm using stack

    self.s = s
    # determine higher scoring substring
    a = ("ab", x) if x > y else ("ba", y)
    b = ("ba", y) if a[0] == "ab" else ("ab", x)

    def remove_ss(ss):
      # returns score by greedily removing ss from s where ss is worth s_ss points
      stack = []
      for c in self.s:
        if stack and stack[-1] + c == ss[0]:
          stack.pop()
        else:
          stack.append(c)
      
      # compute score from this run
      ret = (len(self.s) - len(stack)) // 2 * ss[1]
      # update s
      self.s = ''.join(stack)

      return ret

    return remove_ss(a) + remove_ss(b)

