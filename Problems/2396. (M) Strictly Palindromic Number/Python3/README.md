## 2396. (M) Strictly Palindromic Number

### `solution.py`
At first glance, it would seem that the only solution would be to actually convert `n` into each base and check whether they are palindromic. However we can see that the base `n-2` will **always** result in a value of `12`, which is not palindromic. Thus, an integer that satisfies the problem condition does not exist, and we simply return False in all cases.  

#### Conclusion
This solution has a time and space complexity of $O(1)$.  
  

