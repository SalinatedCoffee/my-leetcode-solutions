class Solution {
  public int minimumDeviation(int[] nums) {
    // max heap based approach

    Queue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
    int min_val = Integer.MAX_VALUE;
    // add all values in max heap, multiply if odd
    int n;
    for (int i = 0; i < nums.length; i++) {
      n = nums[i] % 2 == 1 ? nums[i] * 2 : nums[i];
      pq.add(n);
      min_val = Math.min(min_val, n);
    }

    int min_diff = Integer.MAX_VALUE;
    // while the largest value is even
    while (pq.peek() % 2 == 0) {
      min_diff = Math.min(min_diff, pq.peek() - min_val);
      min_val = Math.min(min_val, pq.peek() / 2);
      pq.add(pq.peek() / 2);
      pq.poll();
    }

    return Math.min(min_diff, pq.peek() - min_val);
  }
}
