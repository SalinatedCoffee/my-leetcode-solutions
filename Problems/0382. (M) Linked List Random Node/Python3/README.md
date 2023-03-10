## 382. (M) Linked List Random Node

### `solution.py`
The naïve method where the list is traversed twice is accepted, and this solution is an implementation of that strategy.  
Upon object initialization we determine the length of the linked list that has `head` as its head by traversing the entirety of it. When `getRandom()` is called, we generate a (uniformly distributed) random number `i` between 1 and the list length and iterate through the list until the `i`th node is reached.  
  
#### Conclusion
Instantiation of `Solution` and calls to `getRandom()` takes $O(n)$ time and $O(1)$ memory, where $n$ is the length of the linked list with `head` as its head. The traversal during initialization takes $O(n)$ time, and retrieving the random `i`th node also takes $O(n)$ time as the list is traversed again.  
This solution obviously has some drawbacks, as it does not support modification of the linked list and it must traverse `i` nodes to retrieve a random `i`th node in the list.  
To optimize the running time, we may use the optimized version of [reservoir sampling](https://en.wikipedia.org/wiki/Reservoir_sampling) which uses the same memory but is much faster than $O(n)$.  
  
