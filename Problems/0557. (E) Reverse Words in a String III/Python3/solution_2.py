class Solution:
  def reverseWords(self, s: str) -> str:
    # one-liner using str.split()
    
    return ' '.join(map(lambda x: x[::-1], s.split()))

