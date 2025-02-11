class Solution:
  def clearDigits(self, s: str) -> str:
    # stack

    stack = []
    for c in s:
      if c in string.ascii_lowercase:
        stack.append(c)
      # it is guaranteed that all digits can be removed
      # so no need to check whether stack is empty
      else:
        stack.pop()

    return ''.join(stack)

