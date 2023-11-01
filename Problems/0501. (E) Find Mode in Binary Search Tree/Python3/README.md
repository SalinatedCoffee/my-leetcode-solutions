## 501. (E) Find Mode in Binary Search Tree

### `solution.py`
The trivial solution would be to simply traverse the entire tree while counting the frequency of the node values. Once the tree has been traversed, we simply sort the node-frequency pairs in descending order of frequency and return the node values with the largest frequencies.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the number of nodes in the tree rooted at `root`. Traversing the entire tree takes $O(n)$ time, and the sorting step takes $O(n\log n)$ time. The space complexity is $O(n)$.  
  

