class Solution:
  def makeGood(self, s: str) -> str:
    # stack

    d = abs(ord('A') - ord('a'))
    stack = []
    for c in s:
      if stack and abs(ord(stack[-1]) - ord(c)) == d:
        stack.pop()
      else:
        stack.append(c)

    return ''.join(stack)

