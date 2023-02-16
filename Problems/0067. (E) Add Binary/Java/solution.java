class Solution {
  public String addBinary(String a, String b) {
    // build string incrementally from LSB

    // for easier string manipulation
    StringBuilder res = new StringBuilder();
    int i = a.length()-1;
    int j = b.length()-1;
    int carry = 0;

    while (i >= 0 || j >= 0) {
      int total = carry;
      // implicit type casting (int + str)
      total += i<0 ? 0:a.charAt(i)-'0';
      total += j<0 ? 0:b.charAt(j)-'0';
      res.append(total%2);
      carry = total>1 ? 1:0;
      i--;
      j--;
    }

    if (carry != 0) {
      res.append("1");
    }

    return res.reverse().toString();
  }
}
