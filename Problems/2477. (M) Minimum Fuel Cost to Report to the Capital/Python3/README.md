## 2477. (M) Minimum Fuel Cost to Report to the Capital

### `solution.py`
We can make things easier to think about if we imagine the representatives that are the furthest away from the capital travels towards it picking up others along the way. Applying this in the context of a tree, this strategy boils down to determining the size of a subtree rooted at a certain node. To do this, we simply implement a recursive DFS traversal that counts the number of nodes. When recursing on the subtrees however we need to remember to compute the consumed fuel for each subtree separately, as there may be cases where leftover seats from one subtree can be filled by reps from other subtrees (for example, imagine 3 subtrees, each with 1 rep on a car with 3 seats).  
To compute the minimum fuel consumption then, we simply recurse starting at the root - in this case, node `0`.

#### Conclusion
This solution takes $O(n)$ time and space to run. The construction of `adj` and DFS traversal via `recurse` takes $O(n)$ time. `adj` and the recursion stack also uses $O(n)$ memory in the worst case.  
  
