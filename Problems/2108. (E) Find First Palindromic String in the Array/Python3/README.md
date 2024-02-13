## 2108. (E) Find First Palindromic String in the Array

### `solution.py`
We simply need to iterate over `words` and return the first string that is palindromic. As a palindrome is essentially a string that is 'mirrored' about the center, reversing the string will yield the same string as the original. Hence we can reverse the string and compare it with the original, and if they are equal we can immediately return the string as it is palindromic.  

#### Conclusion
The time complexity of this solution is $O(mn)$, where $m$ is the average length of the strings in `words` and $n$ is the length of `words`. Reversing a string of length $m$ requires $O(m)$ time to complete, and since all strings in `words` can be reversed in the worst case, the overall time complexity becomes $O(mn)$. The space complexity is $O(m)$ as the reversed string is briefly kept in memory when it is compared to the original string.  
  

