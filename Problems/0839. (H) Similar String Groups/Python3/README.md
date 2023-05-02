## 839. (H) Similar String Groups

### `solution.py`
Thankfully all strings are guaranteed to be permutations of each other, which makes things a lot easier since we can simply compare two strings linearly. To keep track of the grouping of strings we can simply generate a graph, connecting similar strings with an undirected edge. By representing the grouping this way we can count the number of connected components by simply traversing the generated graph. Determining whether two strings are similar is easy; since we know that both strings are anagrams of each other (same letter frequency, same length) we can compare them letter-by-letter and count the number of mismatching pairs. If there are exactly two such pairs, that would mean that we can swap two letters in either string and it would be identical to the other.  
Thus, we first can generate a graph (represented by an adjacency list) by comparing all possible pairs of strings. Then we may traverse the graph (here we have used the iterative flavor of DFS) starting at every node while counting the number of connected components, which we return.  

#### Conclusion
This solution has a time complexity of $O(mn^2)$, where $n$ is the length of `strs` and $m$ is the length of `strs[0]`. There are $n^2 - n$ number of possible string pairs (excluding pairs of the same string), each of which take $O(m)$ time to process. The counting step takes $O(n)$ time as it consists of a single DFS traversal over the generated graph which has $n$ vertices. The space complexity is $O(n^2)$ since strings in `strs` are not guaranteed to be unique, and identical strings are also considered to be similar.  
  
  