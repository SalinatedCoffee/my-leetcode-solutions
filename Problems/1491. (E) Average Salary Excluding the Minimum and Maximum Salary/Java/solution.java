class Solution {
  public double average(int[] salary) {
    // iteration

    int s_min = 100001;
    int s_max = 999;
    int total = 0;
    for (int s: salary) {
      s_min = Math.min(s_min, s);
      s_max = Math.max(s_max, s);
      total += s;
    }
    return (double) (total - s_min - s_max) / (salary.length - 2);
  }
}
