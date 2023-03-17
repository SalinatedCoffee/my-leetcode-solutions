class Solution {
  public int getSum(int a, int b) {
    // bit manipulation

    // limit integers to 4 bytes
    int mask = 0xFFFFFFFF;
    int a_temp = 0;
    int b_temp = 0;

    // half adder logic
    while (b != 0) {
      a_temp = (a ^ b) & mask;
      b_temp = ((a & b) << 1) & mask;
      a = a_temp;
      b = b_temp;
    }
    // two's complement, flip sign as necessary
    return a <= 0x7FFFFFFF ? a : ~(a ^ mask);
  }
}
