## 389. (E) Find the Difference

### `solution.py`
The example test cases given (somewhat annoyingly) all add a character to `s` unshuffled, but this may not be the case. As such, a simple iterative solution that compares character pairs will not work. We may simply count the frequency of each letter that appears in `s` and `t`, but we can greatly simplify this process thanks to how the problem is structured. Here, a valid `t` includes exactly **one** more character than `s`. Hence, if we take the sum of the ASCII codes of both strings and subtract that of `s` from `t`'s, the difference will be the ASCII code of the extra character in `t`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the lengths of `s` and `t`. Each character in both strings is converted to its corresponding ASCII code and is added to the appropriate sum, hence the overall time complexity of $O(m+n)$. The space complexity is also $O(m+n)$, as the ASCII codes are generated using a list comprehension.  
