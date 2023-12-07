## 1903. (E) Largest Odd Number in String

### `solution.py`
We are asked to return the substring of `nums` that contains the largest possible odd number. Because we want to maximize the size of the integer, we also want to select the longest possible substring as it will have more digits(it is guaranteed that `nums` does not contain any leading zeros). This can be achieved by iterating along `nums` in reverse, while checking whether the current digit is odd. If it is, we return the substring that starts at the first character of `nums` and ends at the current character. If not, we move on to the next digit to be examined. When the loop exits normally it means that `nums` does not contain an odd digit and an odd substring does not exist within it. In this case we simply return an empty string, as requested.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. We iterate over `nums` while performing constant time operations for each character. The space complexity is $O(1)$, excluding the returned substring.  
  

