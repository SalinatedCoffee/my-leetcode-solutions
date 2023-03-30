## 87. (H) Scramble String

### `solution.py`
There is no straightforward way to build up to the entire string, so intuition tells us to attempt using top-down dynamic programming. The scrambling process is recursive, where we split two strings and recurse on the resulting substrings. Given a pair of strings we can try all possible splits and recurse on the substrings while memoizing any results that we compute along the way. This can be achieved with a dictionary that maps a tuple of strings to a boolean value. When we recurse, we need to remember to try both configurations where the substrings are either flipped or not flipped.  
  
#### Conclusion
The time complexity is $O(4^n)$ where $n$ is the length of `s1`. `recurse()` iterates along the given string pair, and for each iteration makes up to 4 recursive calls. The space complexity is $O(n^2)$ since the recursion stack will at most be $n$ deep but `memo` can contain all possible substrings of `s1`, which is $n(n+1)/2 = O(n^2)$.  
  

