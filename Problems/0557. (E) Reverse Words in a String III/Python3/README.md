## 557. (E) Reverse Words in a String III

### `solution.py`
The logic to the solution is simple; we split `s` into its constituent words, after which we reverse each word. Then, we construct the string to be returned by concatentating all words while adding a space between an adjacent pair of words.  
While iterating over `s`, we keep track of the starting index of the current word being iterated over. When a space is encountered, we simply take the substring between the starting index and the current position, reverse it, and append it to the end of the return string. Because it is guaranteed that there are no leading or trailing whitespaces we need to manually add the last word to the return string, after which we may return that string directly.  

#### Conclusion
This solution has a time and space complexity of $O(n)$. Because we are utilizing Python slices to obtain substrings of `s`, the space complexity is $O(n)$ instead of $O(1)$.  
  

### `solution_2.py`
We can implement a one-liner solution using Python's many built-in functions. `str.split()` is used to obtain a list of words by splitting `s` with whitespaces, which is given to `map` alongside a lambda function that reverses all words in the list returned by `str.split()`. Finally, we contatentate all reversed words with a whitespace using `str.join()`.  

#### Conclusion
The time and space complexity for this solution is also $O(n)$.  
  

