## 1400. (M) Construct K Palindrome Strings

### `solution.py`
Given the string `s` and integer `k`, we are asked to determine whether all of the characters in `s` can be used to create `k` palindromes. This means that each character in `s` **must** be part of exactly `1` palindromic string.  
Thinking about the problem, we can easily see that it is impossible to create `k` palindromes if `s` has less than `k` characters. We also notice that there is no need to actually construct `k` palindromes, since we are only interested in whether it is possible to do so. To determine this, we first create a frequency list of each unique character in `s`. From there it is not that difficult to see that letters with an odd frequency should each 'seed' an odd length palindrome. If there are more odd frequencies than `k`, it is impossible to create exactly `k` palindromic strings, so we immediately return `False`. Otherwise, it is indeed possible to create `k` palindromes, and we return `True`. We know that this is the case since we have 'spent' `1` character of each unique letter that appears an odd number of times in `s`. This means that the remaining frequency of each and every letter is even, which also means that we can either add them to an existing palindrome or create a new palindromic string.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. `s` is iterated over once in order to generate the frequency list of letters, and since each character takes $O(1)$ time to process, the overall time complexity comes out to be $O(n)$. The space complexity is $O(1)$ because the size of the alphabet of `s` is fixed.  
  

