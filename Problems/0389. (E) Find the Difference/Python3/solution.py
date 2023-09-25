class Solution:
  def findTheDifference(self, s: str, t: str) -> str:
    # convert to and from ascii code

    s_a, t_a = sum([ord(c) for c in s]), sum([ord(c) for c in t])

    return chr(t_a - s_a)

