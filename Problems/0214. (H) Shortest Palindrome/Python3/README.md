## 214. (H) Shortest Palindrome

### `solution.py`
Given the string `s`, we are asked to return the shortest palindrome that can be formed by adding characters in front of `s`. We can obviously make any string into a palindrome through the operation described in the problem. To minimize the number of characters that need to be added, the most optimal method would be to identify the longest palindromic prefix of `s` and append the remaining string reversed in front of `s`. The most simplest method of implementing such an algorithm would be to use brute force, reversing `s` and comparing prefixes of `s` with the suffixes of `s` reversed. To save a little time, we can start comparing the largest pre/suffix pair first which will allow us to exit early as soon as a matching pair is found.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `s`. Reversing `s` requires $O(n)$ time, and comparing each pre/suffix pair also takes $O(n)$ time, which can be performed up to $n$ times. The space complexity is $O(n)$, as the reversed string is kept in memory until the algorithm exits.  
  

