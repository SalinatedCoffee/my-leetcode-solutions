class Solution {
  public int maxProfit(int[] prices) {
    // modified Kadane's algorithm (dynamic programming)

    int min_price = (int) Math.pow(10, 4);
    int max_profit = 0;
    for (int i = 0; i < prices.length; i++) {
      if (prices[i] < min_price)
        min_price = prices[i];
      else
        max_profit = Math.max(max_profit, prices[i] - min_price);
    }
    return max_profit;
  }
}
