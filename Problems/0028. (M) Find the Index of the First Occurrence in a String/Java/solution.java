class Solution {
  public int strStr(String haystack, String needle) {
    // naive solution

    // sanity checks
    if (needle.length() == 0)
      return 0;
    else if (haystack.length() == 0 || haystack.length() < needle.length())
      return -1;
    
    boolean found = false;

    // check against substrings starting at every letter in haystack
    for (int i = 0; i < haystack.length() - needle.length() + 1; i++) {
      for (int j = 0; j < needle.length(); j++) {
        found = true;
        if (haystack.charAt(i+j) != needle.charAt(j)) {
          found = false;
          break;
        }
      }
      if (found)
        return i;
    }
    return -1;
  }
}
