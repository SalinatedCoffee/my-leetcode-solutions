## 1146. (M) Snapshot Array

### `solution.py`
We want to be able to return a value at a certain point of time, and in order to do so we need to associate a snapshot ID to a value stored in the array. This can be trivially accomplished by using a multidimensional array where each index is represented by an array of ID-value pairs. The challenge comes from implementing `get()`, since it can be given any snapshot ID which may not explicitly exist in the index's ID-value array. Assume `set()` has been called two times on some index - once with `snap_id = 1`, `val = 3` and once more with `snap_id = 5`, `val = -22`. If `get()` is called on the same index with `snap_id = 3` then, the return value would be `3` since the index was next updated at `snap_id` `5`, which chronogically comes **after** `snap_id` `3`. That is, we should be returning the value with the **largest** associated ID that is **smaller** than the ID given. This can be efficiently found by using binary search, where the target is the requested ID.  

#### Conclusion
Instantiation of `SnapshotArray` takes $O(m)$ time where $m$ is the size of the array, since the interal array `self.history_records` takes $O(m)$ time to instantiate. Calls to `set()` and `snap()` takes $O(1)$ time. Calls to `get()` will take $O(\log n)$ time where $n$ is the maximum number of method calls made on the `SnapshotArray` object. The number of calls to `set()` is $O(n)$ which means that an index can contain $O(n)$ ID-value pairs, and binary search on a $O(n)$ long list takes $O(\log n)$ time. The space complexity is $O(n)$ for `SnapshotArray` and $O(1)$ for its methods.  
  

