class Solution:
  def minSwaps(self, s: str) -> int:
    # greedy using simulated stack

    hanging = 0
    for c in s:
      match c:
        case '[':
          hanging += 1
        case ']':
          hanging -= 1 if hanging else 0

    return (hanging + 1) // 2

