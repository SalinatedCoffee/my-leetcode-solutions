class Solution {
  public int minFlips(int a, int b, int c) {
    // bit manipulation

    int ret = 0;
    while (a > 0 || b > 0 || c > 0) {
      int c_a = a & 1;
      int c_b = b & 1;
      int c_c = c & 1;
      if (c_c == 1)
        ret += (c_a | c_b) == 0 ? 1 : 0;
      else {
        ret += c_a == 1 ? 1 : 0;
        ret += c_b == 1 ? 1 : 0;
      }
      a >>= 1;
      b >>= 1;
      c >>= 1;
    }
    return ret;
  }
}
