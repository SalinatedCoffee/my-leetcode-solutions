## 152. (M) Maximum Product Subarray

### `solution.py`
Intuition tells us that we could somehow use dynamic programming to solve this problem, as it deals with optimization based on values within continuous subarrays. However we cannot simply compute the products of subarrays recursively since values may be 0 or negative. A valid subarray obviously cannot contain a 0 as the product will also end up as 0. Handling negative numbers is a bit trickier as it may or may not increase the product of the previous subarray, depending on the product's sign. Instead of memoizing the maximum product of subarrays ending at some index (in a list of length `nums`) we can simply keep a running maximum product and a running minimum product. These values will 'flip-flop' between each other while increasing in magnitude as long as a value of 0 is not encountered. At each element we compute the product between it and the running max/min, respectively. We then update the running max/min by selecting the max/min among the current value itself and the two computed products, after which we can update the global maximum value accordingly.  
  
#### Conclusion
This solution takes $O(n)$ time to run where $n$ is the length of `nums`. The space complexity is $O(1)$.  
The solution to this problem isn't very intuitive, and I personally had trouble coming up with a solution. I got to the part where I realized that a list-based DP approach probably wouldn't work but ended up failing to implement a correct solution. At least the solution is short and simple and somewhat easy to understand - that's one more tool that I can use when solving problems like these.  
  
