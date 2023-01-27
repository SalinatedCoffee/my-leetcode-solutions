## 208. (M) Implement Trie (Prefix Tree)
### `solution.py`
Implementing a trie for an alphabet of lowercase English letters is trivial. We define a node class that contains references to its children and whether it is the last letter of a previously inserted word or not.  
  
#### Conclusion
Insertions and lookups take $O(n)$ time, where $n$ is the length of the word. The space complexity is $O(26^n)$ since a node can have at most 26 children, and the depth of a trie is $n$.  
This would be a good problem to revisit, as there are further optimizations that can be made to improve performance.  

