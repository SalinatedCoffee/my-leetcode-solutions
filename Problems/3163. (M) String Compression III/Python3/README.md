## 3163. (M) String Compression III

### `solution.py`
Given the string `word`, we are asked to compress it and return the resulting string. The compression algorithm involves counting the number of consecutive identical characters and appending the count then the letter to the compressed string. If the count exceeds `9`, the count and letter should be appended and the count should be reset. Looking through a few examples, `abcde` should be compressed to `1a1b1c1d1e`, `aaaaaaaaab` to `9a1b`, and `ccccccccccd` to `9c1c1d`. We can easily solve this problem by simply iterating over `word`, while maintaining a counter of identical consecutive characters and the consecutive character itself. Whenever a different character is encountered or the counter would exceed `9`, we update the compressed string appropriately and reset the counter and character. The compressed string is updated one more time after the entirety of `word` has been examined, after which it is directly returned.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `word`. The entirety of `word` is iterated over, with each character taking $O(1)$ time to process. Adding a 'token' onto the compressed string is also a $O(1)$ time operation; and since `word` can be compressed into at most $n$ tokens, the overall time complexity comes out to be $O(n)$. The space complexity is also $O(n)$, as the compressed string is kept in memory in the form of a list of tokens.  
  

