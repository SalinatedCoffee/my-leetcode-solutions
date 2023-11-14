## 1930. (M) Unique Length-3 Palindromic Subsequences

### `solution.py`
Upon seeing the word 'palindromic subsequences' in the title, one would understandably try to implement a dynamic programming based solution. However since we are asked to find palindromes of length 3, we may take a different approach which is also much faster than a hypothetical DP-based solution.  
The critical thing to realize is that there is only one way to construct a 3 character long plaindrome. The first and last letters should be the same, while the middle character can be any letter. Realizing this we can attempt to manually count the number of unique palindromes in `s`. The idea is simple; we find the 'widest' pair for each unique letter in `s` (if it exists) and count the number of unique characters between that pair. To retrieve a list of all unique characters in `s` we initialize a `set` using `s`. Then for each character in the set we scan `s` from either side to find the indices of the first and last occurance of that character in `s`. Now that we know the widest pair we can count the number of unique letters flanked by the pair we found earlier, also using a `set`(though ASCII code based arrays would also work). The number of unique letters is the number of palindromic subsequences we can make, and so we add the value to the total and move on to the next character pair.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `s`. We linearly iterate over `s` for every unique letter in `s`, which is in this case 26. Hence, the time complexity is $O(26n) = O(n)$. The space complexity is $O(1)$ as every `set` used in this problem can at most contain 26 unique letters.  
A possible follow-up to this problem would be where the alphabet of `s` is much larger than 26.  
  

