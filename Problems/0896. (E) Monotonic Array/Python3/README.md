## 896. (E) Monotonic Array

### `solution.py`
Because the array is not guaranteed to be *strictly* increasing, we cannot use binary search to determine its monotonicity. Hence we must resort to a linear-time solution, that checks the 'slope' between all adjacent pairs of values in `nums`. If `nums` has a length of either `1` or `2`, then it is always monotonic, and we can immediately return `True`. If not, we first initialize the sign of the slope between the first two values in `nums`. We then start iterating along `nums`, while computing the slope between all pairs of values as we did for the first pair. If the sign of the current slope is `0`, we skip to the next pair. Otherwise, we look at the sign of the previously computed slopes. If they were `0`, we update the sign to that of the current slope and move on. Else, we determine whether they are the same sign by checking whether their product is negative or not. When we finish iterating over `nums` without prematurely returning, it means that `nums` is indeed monotonic, and we return `True`.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. `nums` is iterated over exactly once, and during each step only a fixed number of constant time operations are performed. The space complexity is $O(1)$.  
  

