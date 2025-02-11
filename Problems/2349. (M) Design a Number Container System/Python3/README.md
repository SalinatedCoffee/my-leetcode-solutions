## 2349. (M) Design a Number Container System

### `solution.py`
We are asked to design a container of numbers that supports the following operations:  

- `change(index, number)` that adds the value `number` at index `index`.  
- `find(number)` that returns the **smallest** index of `number`, or `-1` if the container does not contain `number`.  

Since a single index can contain only 1 value at a time, `change` is trivial to implement - we can use a dictionary that maps each index to its value. `find` is a bit more involved, since we want to return the smallest index of a number. This means that given a value, we want to be able to quickly access the list of indices that contains the value, as well as the smallest index among those indices. As the Python STL does not offer an ordered hash map, we need to use a min heap to store the indices for each number. The problem with this approach is that we can only remove the smallest value from the heap, which means that removing any other value will require popping and storing items on the heap separately until the smallest value in the heap becomes the value we want to remove, after which we add the popped items back onto the heap. To avoid this, we can defer the removals to a later point in time, only doing so when `find` is called. Since we are already keeping track of the value of each index, we can quickly determine whether an index for a given number is valid or not. When `find` is called, we consult this dictionary for the index currently on top of the heap. If it is determined to be invalid, we pop the index off of the heap and try again until we end up with an index that is valid.  

#### Conclusion
Instantiating a `NumberContainers` objects requires $O(1)$ time and memory, as it initially contains 2 empty dictionaries. Over time `NumberContaners` will use $O(n)$ space, where $n$ is the number of calls made to `change`.  
Calls to `change` will finish in $O(\log n)$ time, as the given number will be pushed onto the min heap for the given index, which can contain $O(n)$ elements.  
Finally, calls to `find` requires $O(k\log n)$ time, where $k$ is the number of invalid indices at the time `find` is called.  

