## 1335. (H) Minimum Difficulty of a Job Schedule

### `solution.py`
Essentially, we want to split `jobDifficulty` into `d` subarrays in such a way that the sum of the maximum value of each subarray is minimized. The most straightforward approach involves using dynamic programming, since the original problem can be broken down into smaller problems, and intermediate results may be reused multiple times. For example, if we already know the minimum difficulty when `jobDifficulty[i:]` is split into `j` days, we can use that to determine the value for when `jobDifficulty[i-l:]` is split into `j + 1` days.  
We define a function `recurse(i, j)`, that returns the minimum difficulty of computing the tasks in `jobDifficulty[i:]` across `j` days. When `i == n` there are no more jobs to complete, so we return `0`. When `j == 1` we must complete all remaining jobs in 1 day, so we return the largest value in `jobDifficulty[i:]`. Otherwise, we want to try incrementally completing every possible job in one day. Because we want to leave at least one job for each remaining day, and there would be `j - 1` days remaining after the current day, we can only complete up to the `len(jobDifficulty) - j + 1`th job. Among these splits we choose the split that yields the smallest difficulty, and return the corresponding value.  

#### Conclusion
This solution has a time complexity of $O(n^2d)$ where $n$ is the length of `jobDifficulty` and $d$ is `d`. Each recursion state is represented by 2 integers, one by $n$ and the other by $d$. The time it takes to compute the value of a state is (using the function signature of `recurse`) bound by `i`, which is in turn bound by $n$. Hence, the overall time complexity is $O(n\cdot nd) = O(n^2d)$. The space complexity is $O(nd)$ as we memoize the values of $nd$ states in memory, which outscales the size of the recursion stack.  
  

