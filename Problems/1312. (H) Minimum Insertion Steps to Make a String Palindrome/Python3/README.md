## 1312. (H) Minimum Insertion Steps to Make a String Palindrome

### `solution.py`
First, we need to determine the insertion strategy before figuring out how to compute the desired number of steps using that strategy. Let `s == "abcd"`. The obvious method is to simply reverse the string and concatenate it with its original version (`"abcd" + "dcba" == "abcddcba")`, which would take `n == len(s)` steps. But we can see that the last character of the original string and the first character of the reversed string is always the same, and we can instead ignore the first letter of the reversed string (`"abcd" + "cba" == "abcdcba"`. This would take `n - 1` steps. Assume now that the first and last letters of `s` are the same (modifying the example, `s == "abca"`). Using the naïve method, we would now need to insert `n - 2` letters since the first and last letters already form a palindrome (`abccba` or `acbbca`). But again, the two characters in the center are repeated and thus we can save a step by ignoring one of them. This is because a single character by itself is already a palindrome, so we do not have to insert another character. At this point it becomes clear to us that the minimum number of steps is simply the length of the original string subtracted by the length of its longest palindromic subsequence.  
Now we need to compute the length of the longest palindromic subsequence of `s`. There are $2^{\text{length}(s)}$ possible subsequences of `s` and thus it would not be feasible to brute-force a solution. Instead, we can let `s_rev` be the reverse of string `s` and compute the length of the longest common subsequence between them. This problem can be solved with top-down dynamic programming, which will obviously be much faster than the naïve solution.  

#### Conclusion
\<Content\>  
  

