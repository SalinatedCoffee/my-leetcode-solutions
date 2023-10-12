## 1095. (H) Find in Mountain Array

### `solution.py`
This problem in an extension of [problem 852, Peak Index in a Mountain Array](..%2F..%2F0852.%20%28M%29%20Peak%20Index%20in%20a%20Mountain%20Array). The array can be split into two halves where one is strictly increasing while the other is strictly decreasing. These arrays meet where the peak is, which can be found by using binary search. Since the given mountain array has a maximum length of `10000`, and we make 3 calls to `MountainArray.get()` for each binary search halving, we will end up making at most $\log_2 (10000) \cdot 3 \approx 14 \cdot 3 = 42$ calls when searching for the peak, which is comfortably under the limit of 100 calls. Once the index of the peak has been found, we simply run binary search on each half to find the target. For these searches, only one call to `MountainArray.get()` is required per halving. The worst case is when the peak sits at the center (so the two halves are roughly the same length), and binary search is run on both halves(for this implementation, when `target` exists in the right half). Considering this scenario, a binary search on one half will make at most $\log_2 (5000) \approx 13$ calls to `MountainArray.get()`. Thus the worst-case search for `target` will make 26 'API' calls, which when combined with the peak index search, brings the total to 68 calls.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where $n$ is the length of the array represented by the object `mountain_arr`. Binary search is performed on the array 3 times, with each search taking $O(\log n)$ time to complete (assuming `MountainArray.get()` runs in constant time). The space complexity is $O(1)$.  
  

