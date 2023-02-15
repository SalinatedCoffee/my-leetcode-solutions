## 128. (M) Longest Consecutive Sequence

### `solution.py`
Since we are restricted to a runtime of $O(n)$, any approaches that use sorting are off the table (the 'linear' sorting algorithms would use too much memory). The problem asks us to find the length of a *consecutive* sequence, which means that given some number we know what its previous and next numbers would be if `nums` was sorted. Could we somehow verify that those numbers are in `nums` in constant time? Absolutely - we can simply convert `nums` into a set (duplicate numbers are not counted) and check if `n-1` or `n+1` is in that set given some number `n`.  
Now that we can access the neighboring numbers in constant time, we can determine the length of the consecutive sequence that contains `n`. However the set is not sorted, and simply counting the sequence length for all numbers would result in a runtime of $O(n^2)$. What we can do here is to think of the first element in a sequence as its unique 'identifier', and only start counting when some number is the smallest element in its sequence. This can be trivially checked by verifying whether `n-1` is in the set for some number `n`, as sequences have to be comprised of consecutive numbers. So iterating over `nums`, the solution starts counting up when `n-1` is not in `nums` and skip if otherwise.  
  
#### Conclusion
This solution takes $O(n)$ time to run and uses $O(n)$ space, where $n$ is the length of `nums`. All elements in `nums` are touched exactly once, taking $O(1)$ time per element. `nums_set` uses $O(n)$ space as it is simply a hash table of `nums`.  
Notice that this turns into a BFS problem if we had decided to keep track of numbers that we have already counted, and expanded outwards from both sides of some number. The hash-based approach taken here also has some semblance to union find in that the solution groups items into several disjoint sets (in this case implicitly).  
  
