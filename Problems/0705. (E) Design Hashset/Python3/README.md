## 705. (E) Design HashSet

### `solution.py`
"Design a hash table *without* using any built-in libraries." is an extremely loaded question, but this problem being labeled easy lets us get away with implementing a very naïve data structure. Since the input domain is well defined and has a limited range, we can simply preallocate a list to keep track of the elements that have been inserted. The input space is $[0, 10^6]$, so we initialize a $1000 \times 1000$ 2D list named `items` in which we store the inserted elements. A separate instance variable is used to store the maximum value $10^6$ explicity.  
  
#### Conclusion
Instantiating `MyHashSet` takes $O(n^{1/2})$ time, where $n$ is the size of the input domain. An array of fixed size $\sqrt{n}$ is instantiated with the object, hence the sub-linear time complexity.  
Calls to `add()`, `contains()`, and `remove()` also takes $O(n^{1/2})$ time (assuming integer division takes constant time) since the nested 'mod' list is linearly scanned for `key`, and may contain at most $n^{1/2}$ elements. Note that `add()` and `remove()` performs an extra $O(n^{1/2})$ operation, making them slower than `contains()`.  
The overall space complexity of `MyHashSet` is $O(n)$, since it stores each element explicitly.  
