class Solution {
  public double average(int[] salary) {
  // sort

  Arrays.sort(salary);
  return (double) Arrays.stream(salary, 1, salary.length-1).sum() / (salary.length-2);
  }
}
