## 17. (M) Letter Combinations of a Phone Number

### `solution.py`
We see that this problem can be trivially solved with recursion, since the original problem can clearly be divided into smaller subproblems. For some digit string `digits`, we know that the first digit can be converted into one of its corresponding characters on a keypad. The problem wants us to find all possible string representations of `digits`, so naturally we should be trying all possible conversions of that specific digit. If we select a valid character for `digits[0]`, we now need to convert `digits[1:]`. At this point we can clearly see that we can apply the same principle described above on this suffix substring as well, as well as the next suffix substring `digits[2:]` and so on. We backtrack when a recursive call is made with an empty string, since there are no more digits to convert.  

#### Conclusion
The time complexity of this solution is $O(4^n)$, where $n$ is the length of the string `digits`. For each digit we have at most 4 possible characters to choose from, which we try selecting each and every one. The space complexity (excluding the return object `self.ret`) is $O(n)$, since the maximum recursion depth is $n$.  
  

