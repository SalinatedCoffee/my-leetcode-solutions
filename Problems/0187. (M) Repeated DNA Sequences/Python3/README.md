## 187. (M) Repeated DNA Sequences

### `solution.py`
Given a string `s`, we are asked to return a list of all recurring substrings of length 10. To solve this problem, we can simply store the number of occurrences for each unique substring and only return those that appear more than once. As the size of the substrings is fixed, each hash operation can be considered as taking constant time, making this approach a viable solution.  
The counts of each substring will be stored in the dictionary `seen`, where the keys are the substrings of `s` and the values the number of appearences of those substrings in `s`. `s` is then iterated over, while taking a 10-character-long slice of `s` and looking it up in `seen`. Once all substrings have been examined, we iterate over the key-value pairs of `seen` and add the keys that have a value of greater than `1` to the return list `ret`.  

#### Conclusion
This solution has a time complexity of $O(n)$, wher $n$ is the length of the string `s`. All substrings of `s` that are 10 characters long are examined by iterating over `s`. As previously mentioned, hashing is a linear time operation in terms of the length of the input. But as all keys have a fixed size of 10 characters, these operations can be considered as taking $O(1)$ time to complete. Hence, the overall time complexity is $O(n)$. The space complexity is also $O(n)$, due to the dictionary `seen`.  
  

