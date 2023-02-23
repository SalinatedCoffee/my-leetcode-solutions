## 211. (M) Design Add and Search Words Data Structure

### `solution.py`
Our data structure needs to support partial wildcard searches, which means a modified prefix tree (trie) would work perfectly in this situation. The underlying structure can be left as-is, but the search method needs to be modified to support wildcard characters. This is fortunately quite trivial - if we change the signature of `search()` so that it accepts an optional parameter `node` from where it will start matching characters of `word`, we can recurse on all available children of a node whenever we encounter the character `.`.  

#### Conclusion
For `addWord()`, the time and space complexity is $O(n)$ where $n$ is the length of the word. This is because $n$ nodes will be created in the trie in the worst case.  
For `search()`, the time complexity is $O(26^3n) = O(n)$ since a node can have up to 26 children and a given word can at most contain up to 3 wildcard characters. The space complexity is $O(3) = O(1)$ as the recursion stack will at most be 3 levels deep.  
`WordDictionary` uses $O(26^k)$ memory where $k$ is the average length of all words stored in the trie, as all nodes use a list of size 26 regardless of the number of children they have.  
