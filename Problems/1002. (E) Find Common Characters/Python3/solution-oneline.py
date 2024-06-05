class Solution:
  def commonChars(self, words: List[str]) -> List[str]:
    # one-liner using https://docs.python.org/3/library/collections.html#collections.Counter.elements

    # convert word to Counter object, compute intersection, and generate list of common characters
    return reduce(lambda x, y: x & y, map(Counter, words)).elements()

