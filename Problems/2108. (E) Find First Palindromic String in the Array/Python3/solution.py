class Solution:
  def firstPalindrome(self, words: List[str]) -> str:
    # reverse string

    for word in words:
      if word == word[::-1]:
        return word

    return ""

