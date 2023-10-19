class Solution:
  def backspaceCompare(self, s: str, t: str) -> bool:
    # stacks

    def process(st):
      stack = []
      for c in st:
        if c != '#':
          stack.append(c)
        elif stack:
          stack.pop()
      
      return ''.join(stack)
    
    return process(s) == process(t)

