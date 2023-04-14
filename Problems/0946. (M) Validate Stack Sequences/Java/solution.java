class Solution {
  public boolean validateStackSequences(int[] pushed, int[] popped) {
    // stack with two pointers

    int pop_ptr = 0;
    Deque<Integer> stack = new ArrayDeque();
    for(int i = 0; i < pushed.length; i++) {
      stack.push(pushed[i]);
      // keep matching until mismatch detected
      while (stack.size() > 0 && pop_ptr < popped.length && stack.peek() == popped[pop_ptr]) {
        stack.pop();
        pop_ptr++;
      }
    }
    return popped.length == pop_ptr;
  }
}
