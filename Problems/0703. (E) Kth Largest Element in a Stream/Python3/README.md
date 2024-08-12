## 703. (E) Kth Largest Element in a Stream

### `solution.py`

We need to store the current k largest elements in a way that we can access the smallest element quickly. Heaps are a perfect fit for this, as they support efficient inserts / removals while allowing us to access the smallest element in optimal time (Python `heapq`s are min-heaps). When the object is instantiated we simply sort the input array and save a slice containing the k largest elements. The only values we are interested is are the k largest values seen up to this point, and thus when `.add()` is called with an argument that is smaller than the smallest value in `self._items` we can simply do nothing and simply return the smallest value of `self._items`. Otherwise we push the value on the heap, pop a value from the heap, and return it (combined into a single call to `heapreplace()`).  

One small detail to take care of is that `self._items` may not contain k elements after the object has been freshly instantiated. We account for that edge case by also keeping track of what length `self._items` should be and comparing it whenever `.add()` is called.  

#### Conclusion

Instantiation will take $O(n\log n)$ time to run, where $n$ is the length of `nums`. `nums` is sorted, after which a slice of it is turned into a heap - these are both operations that take $O(n\log n)$ time. Calls to `.add()` will take $O(\log k)$ time where $k$ is simply `k`. In the worst case a single push and a single pop operation will be executed on `self._items`, each of which takes $O(\log k)$ time. The space complexity is $O(n)$ during instantiation (sorting takes $O(n)$ space) and $O(k)$ throughout the lifespan of the object.  



### `solution_2.py`
In the previous solution we pre-sorted `nums` in order to get rid of any elements less than the `k`th largest element, after which we converted the remaining values into a heap. Here we can see that the sorting step is not needed, as converting `nums` into a heap will allow us to access its contents in ascending order. When a `KthLargest` object is initialized, we now convert the entirety of `nums` to a heap. The previous solution enforced the length of `self._items` in the constructor. Because we have removed the sorting step we need to enforce this somewhere else. We can do this in `.add()` by first inserting `val` into `nums`(which is necessary since `self._items` may be empty) and then popping items off of the heap until its length is equal to `self._k`. After these steps, the item on top of the heap will be the desired value.  

#### Conclusion
Instantiation requires $O(n\log n)$ time to complete, since the entirety of `nums` is converted into a min heap. Subsequent calls to `.add()` will each take $O(\log k)$ to complete since `self._items` is guaranteed to contain at most $n$ elements. The first call to `.add()` reduces this number to $k$, which stays constant over the lifecycle of the `KthLargest` object.  