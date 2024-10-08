class Solution:
  def minSwaps(self, s: str) -> int:
    # greedy using stack

    stack = []
    hanging = 0
    for c in s:
      match c:
        case '[':
          stack.append(c)
        case ']':
          if stack:
            stack.pop()
          else:
            hanging += 1

    return (hanging + 1) // 2

