class Solution {
  public int compress(char[] chars) {
    // two pointers, process letters by group

    // points to first unprocessed letter
    int end_idx = 0;
    int cur_idx = 0;
    char counting = chars[0];
    while (cur_idx < chars.length) {
      int count = 1;
      // count current group of letters
      while (cur_idx+count < chars.length &&
             chars[cur_idx+count] == chars[cur_idx])
        count++;
      // append letter being counted to end of compressed string
      chars[end_idx] = chars[cur_idx];
      end_idx++;
      // append letter count to end of previous
      if (count > 1) {
        String str_count = Integer.toString(count);
        // array assignments unsupported in Java, do it manually
        for (int i = 0; i < str_count.length(); i++)
          chars[end_idx+i] = str_count.charAt(i);
        end_idx += str_count.length();
      }
      // advance current index
      cur_idx += count;
    }
    return end_idx;
  }
}
