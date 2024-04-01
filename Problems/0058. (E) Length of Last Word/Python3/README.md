## 58. (E) Length of Last Word

### `solution.py`
As we want the length of the last word, with a word being a string of consecutive non-whitespace characters, we can simply iterate over `str` in reverse. Because `str` may contain trailing whitespace, we iterate over `str` in two parts; once to skip any whitespace at the end of `str`, and twice to count the number of characters in the last word of `str`. This can easily be achieved by using a while loop. The first loop skips over any trailing whitespace, and the second counts the number of consecutive characters after.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `str`. In the worst case where `str` only contains a single word without any leading whitespace, `str` will be iterated over exactly once with each character taking $O(1)$ time to process. The space complexity is $O(1)$.  
  

### `solution_2.py`
Instead of manually traversing `str`, we can use the many built in string methods in Python to make our job considerably easier. `str` is first split into substrings where the character `' '` is used as the delimiter using the string method `string.split()`. The resulting list is then traversed in reverse using `reverse()` to find the first non-empty substring, after which its length is immediately returned.  

#### Conclusion
The time complexity of this solution is $O(n)$. `string.split()` splits `str` into multiple substrings, and takes $O(n)$ to complete. The space complexity is also $O(n)$, because `string.split()` splits `str` into the appropriate substrings the moment it is called(returns a list instead of a generator) which means that **all** of the split substrings are kept in memory.  
  

