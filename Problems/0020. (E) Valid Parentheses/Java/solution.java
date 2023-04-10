class Solution {
  public boolean isValid(String s) {
    // stack

    Deque<Character> stack = new ArrayDeque();
    for (int i = 0; i < s.length(); i++) {
      char c = s.charAt(i);
      if (c == '(' || c == '{' || c == '[')
        stack.push(c);
      else {
        // check if closed parentheses match against top of stack
        if (stack.size() == 0)
          return false;
        char m = stack.pop();
        // switch-case(break)
        switch (c) {
          case ')':
            if (m != '(') return false;
            break;
          case '}':
            if (m != '{') return false;
            break;
          case ']':
            if (m != '[') return false;
            break;
        }
      }
    }
    return stack.size() == 0;
  }
}
