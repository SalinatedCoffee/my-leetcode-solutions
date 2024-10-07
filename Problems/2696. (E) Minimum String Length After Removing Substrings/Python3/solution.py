class Solution:
  def minLength(self, s: str) -> int:
    # stack

    chars = []
    for c in s:
      # if top-most item on stack and current character form "AB" or "CD", remove them
      if len(chars) > 0 and ((chars[-1] == 'A' and c == 'B') or (chars[-1] == 'C' and c == 'D')):
        chars.pop()
      else:
        chars.append(c)

    return len(chars)

