## 703. (E) Kth Largest Element in a Stream

### `solution.py`

We need to store the current k largest elements in a way that we can access the smallest element quickly. Heaps are a perfect fit for this, as they support efficient inserts / removals while allowing us to access the smallest element in optimal time (Python `heapq`s are min-heaps). When the object is instantiated we simply sort the input array and save a slice containing the k largest elements. The only values we are interested is are the k largest values seen up to this point, and thus when `.add()` is called with an argument that is smaller than the smallest value in `self._items` we can simply do nothing and simply return the smallest value of `self._items`. Otherwise we push the value on the heap, pop a value from the heap, and return it (combined into a single call to `.heapreplace()`).  

One small detail to take care of is that `self._items` may not contain k elements after the object has been freshly instantiated. We account for that edge case by also keeping track of what length `self._items` should be and comparing it whenever `.add()` is called.  

#### Conclusion

Instantiation will take $O(n\log n)$ time to run, where $n$ is the length of `nums`. `nums` is sorted, after which a slice of it is turned into a heap - these are both operations that take $O(n\log n)$ time. Calls to `.add()` will take $O(\log k)$ time where $k$ is simply `k`. In the worst case a single push and a single pop operation will be executed on `self._items`, each of which takes $O(\log k)$ time. The space complexity is $O(n)$ during instantiation (sorting takes $O(n)$ space) and $O(k)$ throughout the lifespan of the object.  


