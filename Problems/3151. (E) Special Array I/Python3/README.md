## 3151. (E) Special Array I

### `solution.py`
An array is considered special if all pairs of its adjacent elements have a different parity('odd-ness') or if it does not contain any adjacent pairs. Given the list of integers `nums`, we are asked to determine whether it is a special array or not. Because `nums` is short, we can trivially solve the problem by iterating over `nums` to check all possible adjacent pairs. Whenever we detect a pair that has the same parity, we immediately return `False`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

