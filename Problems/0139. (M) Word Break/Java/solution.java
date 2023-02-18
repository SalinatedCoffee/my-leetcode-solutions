class Solution {
  public boolean wordBreak(String s, List<String> wordDict) {
    // optimized dp solution using hashsets

    // declare variable type as generic version of actual instantiation
    Set<String> words = new HashSet<>(wordDict);

    // arrays use .length (prop)
    // strings (java.lang.String) use .length() (method)
    // objects in java.util.Collection use .size() (method)
    boolean[] dp = new boolean[s.length()+1];
    // Java arrays are initialized with a default value based on type
    // For booleans, default is false
    //Arrays.fill(dp, false);
    dp[0] = true;

    for (int i=1; i < s.length()+1; i++) {
      for (int j=0; j < i; j++) {
        if (dp[j] && words.contains(s.substring(j,i))) {
          dp[i] = true;
          break;
        }
      }
    }
    return dp[s.length()];
  }
}
