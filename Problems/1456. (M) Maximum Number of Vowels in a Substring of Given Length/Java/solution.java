class Solution {
  public int maxVowels(String s, int k) {
    // sliding window

    int cur = 0;
    Set<Character> vowels = new HashSet();
    char[] t = {'a', 'e', 'i', 'o', 'u'};
    for (char c: t)
      vowels.add(c);
    for (int i = 0; i < k; i++){
      if (vowels.contains(s.charAt(i)))
        cur++;
    }

    int ret = cur;
    for (int i = k; i < s.length(); i++) {
      if (vowels.contains(s.charAt(i-k)))
        cur--;
      if (vowels.contains(s.charAt(i)))
        cur++;
      ret = Math.max(ret, cur);
    }
    return ret;
  }
}
