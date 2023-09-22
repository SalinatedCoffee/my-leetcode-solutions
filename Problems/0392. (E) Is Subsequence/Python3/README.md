## 392. (E) Is Subsequence

### `solution.py`
The trivial solution is to simply 'consume' each character in `s` while iterating along `t`. A character is 'consumed' when the current character in `s` matches the current character in `t`. If the entierety of `s` is matched, then it is a subsequence of `t`. Otherwise it is not, and we return `False`.  

#### Conclusion
This solution has a time complexity of $O(n)$, $n$ is the length of `t`. `s` and `t` are traversed simultaneously, but the length of `s` is bound by `t` - hence the running time of $O(n)$. The space complexity is $O(1)$.  
The follow-up question asks about validating against multiple candidate subsequences, which is exactly problem [#792, Number of Matching Subsequences](https://leetcode.com/problems/number-of-matching-subsequences).  

