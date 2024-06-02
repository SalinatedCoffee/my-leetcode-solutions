## 3110. (E) Score of a String

### `solution.py`
Since the score of a string is simply the sum of the absolute difference of the ASCII values of each adjacent pair of characters in `s`, this can trivially be computed by making a single pass over `s` starting at the `1`st element of `s`(0-indexed) while computing the absolute ASCII difference between the current and previous character.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `s`. A single pass is made over `s`, and each adjacent character pair takes $O(1)$ time to process. The space complexity is $O(1)$.  
  

