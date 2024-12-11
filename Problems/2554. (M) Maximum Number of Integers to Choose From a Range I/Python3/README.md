## 2554. (M) Maximum Number of Integers to Choose From a Range I

### `solution.py`
Given the integer `n`, we can select any number of integers in the range `[1, n]`. Each integer can be selected at most once, and can be selected only if it is not in the list of integers `banned`. If the sum of the selected integers cannot exceed `maxSum`, our task is to determine the maximum number of integers that can be selected when given `n`, `banned`, and `maxSum`.  
Because we want to select as many integers as possible while staying under the limit of `maxSum`, we would obviously want to prioritize choosing the smaller values first. We also want to be able to determine whether an integer is banned or not in constant time, which can be trivially accomplished by populating a set with the contents of `banned`. As we are given a range in which to choose integers from, we can iterate over this range while greedily selecting available integers, stopping whenever the sum exceeds `maxSum`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ is the length of `banned` and $n$ is `n`. Populating a set with `banned` requires $O(m)$ time to complete. Iterating over the range `[1, n]` takes $O(n)$ time as each integer is processed in $O(1)$ time. The space complexity is $O(m)$, due to `banned`.  
  

