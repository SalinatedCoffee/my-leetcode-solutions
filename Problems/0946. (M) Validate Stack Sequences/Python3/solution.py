class Solution:
  def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    # stack with two pointers

    pop_ptr = 0
    stack = []
    for i in range(len(pushed)):
      stack.append(pushed[i])
      # keep matching until mismatch detected
      while stack and pop_ptr < len(popped) and stack[-1] == popped[pop_ptr]:
        stack.pop()
        pop_ptr += 1
    
    return len(popped) == pop_ptr

