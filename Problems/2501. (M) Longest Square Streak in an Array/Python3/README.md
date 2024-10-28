## 2501. (M) Longest Square Streak in an Array

### `solution.py`
Given the list of integers `nums`, we are asked to return the length of the longest square streak. A square streak is a subsequence of `nums` that is at least 2 elements long, and when sorted in ascending order each element is the square of the previous element. For example, if `nums = [4, 3, 6, 16, 8, 2]`, the longest square streak would be `4, 16, 2` as it is 3 elements long, and when sorted becomes `2, 4, 16`.  
Immediately we can see that a brute force solution is possible as we can sequentially generate the values of the subsequence candidates given some starting value. In order to quickly determine whether a candidate is indeed an element of `nums`, we can convert `nums` into the set `nums_set`. Each element of `nums` is used as a starting point of a potential subsequence. After squaring the current value, `nums_set` is consulted to determine whether the squared value exists in `nums`. If so, the length of the subsequence is increased by `1` and the current value becomes the squared value. These steps are repeated until the current value is determined to be not an element of `nums`, at which point we update the previous longest subsequence length as necessary and move on to the next element in `nums` to be used as a starting point.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the length of `nums`. Instantiating `nums_set` using `nums` takes $O(n)$ time. The square streak computation step that follows uses each element within `nums` as the starting point. Since generating a candidate takes $O(1)$ time, and the length of a square streak is bound by $n$, this step will take $O(n^2)$ time to complete. The space complexity is $O(n)$, as `nums_set` is kept in memory until the algorithm exits.  
  

