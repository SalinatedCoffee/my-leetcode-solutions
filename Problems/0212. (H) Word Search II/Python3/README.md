## 212. (H) Word Search II

### `TLE.py`
We can obviously traverse `board` with DFS, but we need to come up with a method to efficiently determine whether a word is in `words`. The instinct is to simply use Python sets. This will work, but upon further contemplation this will result in many unnecessary lookups (for `words = ['apple']` the algorithm will constantly look up words with prefix `'xyz'` even though it does not exist). To solve this we can use tries, backtracking early whenever we detect that the current prefix does not exist in the trie.  
This algorithm populates a trie with the contents of `words` and then uses DFS traversal to check whether a word from `board` exists in `words`. We store matches in a Python set as the problem does not allow duplicates in the return list.  
  
#### Conclusion
This algorithm times out on sufficiently large inputs, and on inputs where most words share the same prefix.  
  

### `solution.py`
There are many optimizations that can be made to the previous algorithm - namely, we can perform the DFS traversal and trie traversals simultaneously, and switch to a dictionary-based trie instead of classes. We can also 'delete' a word once it has been found, eliminating the need to use a set to store matching words.  
With all of these (and more) optimizations implmented, this solution passes the online judge.  
  
#### Conclusion
The time complexity is $O(mn4^w)$, where $m$, $n$ are the dimensions of `board`, and `w` is the average length of a word in `words`.  
The space complexity is $O(26^w)$.  
  
