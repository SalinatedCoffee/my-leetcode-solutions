class Solution {
  public int addDigits(int num) {
    // base 10 digital root

    return num == 0 ? 0 : 1 + ((num-1) % 9);
  }
}
