class Solution {
  public String simplifyPath(String path) {
    // stack

    Deque<String> dirs = new ArrayDeque();
    String[] tokens = path.split("/");
    for (String t: tokens) {
      if (t.length() == 0 || t.equals("."))
        continue;
      if (t.equals("..")) {
        if (dirs.size() > 0)
          dirs.pop();
      }
      else
        dirs.push(t);
    }
    String ret = "";
    while (dirs.size() > 0)
      ret += "/" + dirs.removeLast();
    return ret.length() > 0 ? ret : "/";
  }
}
