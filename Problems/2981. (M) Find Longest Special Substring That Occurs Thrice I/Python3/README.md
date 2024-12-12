## 2981. (M) Find Longest Special Substring That Occurs Thrice I

### `solution.py`
A string is special if it is comprised of only a single character. The strings `a`, `zzz`, and `llllll` are all considered to be special. Given the string `s`, we are asked to return the length of the longest special substring that appears in `s` at least 3 times. If such a substring does not exist, we should return `-1`.  
Because the size constraint on `s` is tiny, we know that we can take a very heavy-handed solution in terms of computation and still get away with it. That is, a brute force solution that generates all substrings of `s` and keeps tallies on the special strings is a viable approach for this problem. The idea is simple; we generate all possible substrings of `s`, evaluate the specialness of each substring, and update the counter for that substring if it is special. Once all substrings have been examined, we iterate over the counters of each special substring to determine the length of the longest substring that has a count greater than or equal to `3`. The first two steps are very straightforward to implement using a handful of for loops and conditionals. When counting the special strings, we use a dictionary to store the counts, and iterate over the key-value pairs after all substrings have been examined.  

#### Conclusion
This solution has a time complexity of $O(n^3)$, where $n$ is the length of `s`. There are $O(n^2)$ possible substrings of `s`, with each requiring $O(n)$ time to determine its specialness. Iterating over the key-value pairs of the dictionary containing the substring counts takes $O(n^2)$ time, putting the overall time complexity of this solution at $O(n^3)$. The space complexity is $O(n^2)$, due to the dictionary of counts `freq`.  
  

