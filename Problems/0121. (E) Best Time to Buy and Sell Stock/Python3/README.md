## 121. (E) Best Time to Buy and Sell Stock

### `solution.py`
Thankfully we can only move forward through `prices`, so we don't have to consider purchase/sell combinations where a sell occurs before a purchase. Now we want to maximize the difference between the smallest number in the range $[0, i]$ and the largest number in the range $(i, n)$. The thing to realize here is that the smallest number in the range $[0, i]$ will not change if there are no numbers smaller than that in the range $(i, n)$. So we can simply iterate through `prices` and either update the smallest number seen or see whether the difference between the smallest number and the current one is larger than the value we had previously.  
  
#### Conclusion
This solution takes $O(n)$ time to run where `n` is the length of `prices`. The space complexity is $O(1)$.  
Notice that this is just a modified version of Kadane's algorithm (maximum subarray problem).  
  
