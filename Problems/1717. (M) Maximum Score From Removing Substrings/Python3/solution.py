class Solution:
  def maximumGain(self, s: str, x: int, y: int) -> int:
    # greedy algorithm using stack

    self.s = s
    # determine higher scoring substring
    a = "ab" if x > y else "ba"
    b = "ba" if x == "ab" else "ab"

    def remove_ss(ss, s_ss):
      # returns score by greedily removing ss from s where ss is worth s_ss points
      stack = []
      for c in self.s:
        if stack and stack[-1] + c == ss:
          stack.pop()
        else:
          stack.append(c)
      
      # compute score from this run
      ret = (len(self.s) - len(stack)) // 2 * s_ss
      # update s
      self.s = ''.join(stack)

      return ret

    return remove_ss(a, max(x, y)) + remove_ss(b, min(x, y))

