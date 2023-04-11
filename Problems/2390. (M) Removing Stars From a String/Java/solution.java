class Solution {
  public String removeStars(String s) {
    // stack

    Deque<Character> stack = new ArrayDeque();
    for (int i = 0; i < s.length(); i++) {
      if (s.charAt(i) != '*')
        stack.push(s.charAt(i));
      else
        stack.pop();
    }
    String ret = "";
    while (stack.size() > 0)
      // no straightforward way to convert ArrayDeque<Character> into String
      // so do it manually
      // for some weird reason, Java uses the left-hand side as the top of the stack
      // so append items starting from right-most char
      ret += stack.removeLast();
    return ret;
  }
}
