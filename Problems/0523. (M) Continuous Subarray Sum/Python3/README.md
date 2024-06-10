## 523. (M) Continuous Subarray Sum

### `solution.py`
If you have solved [problem 974, 'Subarray Sums Divisible by K'](../../0974.%20%28M%29%20Subarray%20Sums%20Divisible%20by%20K), this problem should also be pretty straightforward to solve. Essentially, if a prefix sum modulo some value is `i`, we can 'cancel out' the remainder if the prefix has a prefix where its sum modulo that value is also `i`. Using this property we can store whether a prefix sum modulo `k` has been seen in a set(since `k` can be very large, using a list will fail with MLE) which we can consult after computing the prefix sum mod `k` up to the current element being considered. If it exists in the set, a subarray divisible by `k` exists in `nums` and we return `True`. Otherwise, we simply move on to the next element. The main difference between this problem and problem 974 is that here, a subarray must be at least 2 long. Thus, we need to make sure that the set of prefix sums reflects that of 2 elements prior to the current one. We maintain a separate variable `prefix_mod_lag` that keeps track of the prefix sum 2 elements before the current item being considered. The set of prefix sums are updated using this variable, whereas it is checked against the current prefix sum, `prefix_mod`.  
Once all elements in `nums` have been examined, we do a final check on the set of prefix sums and return `True` if the prefix sum mod `k` exists.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. No precomputation is performed, and the initialization of all variables and data structures take $O(1)$ time. While `nums` is iterated over, each element also takes $O(1)$ time to process, bringing the overall time complexity to $O(n)$. The space complexity is $O(k)$, where $k$ is `k`. Since the set `mods` contains the results of any value modulo `k`, it can at most contain $k$ items(all integers in the interval $[0, k)$).  
  

