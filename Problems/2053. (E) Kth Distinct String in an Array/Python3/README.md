## 2053. (E) Kth Distinct String in an Array

### `solution.py`
From the list of strings `arr`, we are asked to return the `k`th(1-indexed) unique string. Straight away we know that we would have to examine the entirety of `arr` to determine the uniqueness of each string. Because we are dealing with strings, we also know that we should use a dictionary to keep track of this information. Python dictionaries guarantee that the insertion order is preserved, which means that if we iterate over `arr` from left to right while inserting key-value pairs into a dictionary, iterating over the dictionary will yield the unique strings in order of their appearance in `arr`. Using this, we can decrement `k` whenever a unique string has been found, returning the string whenever it reaches `0`. If `k` is not `0` even after iterating over the key-value pairs, it means that there are less than `k` unique strings and we return an empty string.  

#### Conclusion
This solution has a time complexity of $O(mn)$ where $n$ is the length of `arr` and $m$ is the average length of the strings in `arr`. Each string in `arr` is hashed, and because this operation takes $O(m)$ time to complete on a string of length $m$, the overall time complexity becomes $O(mn)$. The space complexity is also $O(mn)$, due to the dictionary `strs`.  
  

