## 2870. (M) Minimum Number of Operations to Make Array Empty

### `solution.py`
The first instinct would be to use dynamic programming to incrementally build up to the answer. Each recursive state would try removing either 2 or 3 numbers until `nums` is empty, among which we would select the option that requires the smallest number of operations. However, because the two operations that we can perform only differ by 1, we can directly compute the number of operations to remove a number from `nums` given its frequency count. As we want to minimize the number of total operations performed, it is obviously optimal to remove numbers in triplets as much as possible. Given some integer `i` that corresponds to the number of occurrences of some number in `nums`, we try dividing it by `3`. If `i` is divisible by `3`, we add the quotient to the sum of all previously deleted numbers and move on. Otherwise, we add `1` to the quotient, and add that to the sum. This can be trivially proven, but the gist is that an extra operation is required regardless of whether the remainder is `1` or `2`. We also have to remember to check for the case where the number is not deletable, which is when there is only one instance of that number in `nums`. Whenever this is the case, `nums` cannot possibly be emptied using the two operations, and so we can immediately return `-1`. After all values have been removed, we simply return the sum of operations performed.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `nums`. Each value of `nums` is counted using a Python `Counter`, which takes $O(n)$ time. Determining the number of operations also take $O(n)$ time, assuming that division and modulo operations all take $O(1)$ time to perform. The space complexity is $O(n)$, as we keep the frequency count of each unique number in `nums` in memory using a `Counter`.  
  
