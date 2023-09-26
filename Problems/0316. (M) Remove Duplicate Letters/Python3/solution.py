class Solution:
  def removeDuplicateLetters(self, s: str) -> str:
    # greedy algorithm using stack

    n = len(s)
    last = defaultdict(int)
    for i in range(n):
      last[s[i]] = i
    
    letters = []
    in_stack = set()
    for i in range(n):
      if s[i] not in in_stack:
        while (letters and letters[-1] > s[i] and last[letters[-1]] > i):
          in_stack.remove(letters.pop())
        letters.append(s[i])
        in_stack.add(s[i])
    
    return ''.join(letters)

