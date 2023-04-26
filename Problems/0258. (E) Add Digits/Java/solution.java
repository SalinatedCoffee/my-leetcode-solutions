class Solution {
  public int addDigits(int num) {
    // iteration

    int ret = 0;
    while (true) {
      ret += num % 10;
      num /= 10;
      if (num == 0) {
        if (ret < 10)
          break;
        num = ret;
        ret = 0;
      }
    }
    return ret;
  }
}
