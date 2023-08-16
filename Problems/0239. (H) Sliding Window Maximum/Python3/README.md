## 239. (H) Sliding Window Maximum

### `TLE.py`
An obvious solution would be to scan the window for its maximum value for every possible window. Because we do not use a separate data structure to represent the window, the search will be a linear time operation.  

#### Conclusion
The time complexity is $O(nk)$, where $n$ is the length of `nums` and $k$ is `k`. There are $n-k$ windows of length `k`, for each of which we perform a linear scan for its maximum value. Hence, the overall time complexity will be $O((n-k)k) = O(nk - k^2) = O(nk)$(since $k$ is bound by $n$). The space complexity is $O(1)$ (ignoring memory used by list slicing).  
  


### `solution.py`
The first approach, while correct, takes too long to run and fails with TLE. We cannot (at least in a straightforward way) save time in advancing the window, which means that we can likely reduce the time complexity in determining the window maximum value. Binary search is not viable as the window is not sorted, which leads us to the next logarithmic approach - heaps. By representing the sliding window with a heap we can access the largest value in constant time, and perform insertions and deletions in logarithmic time. However if we try to naïvely maintain the heap so that its contents only contain the elements in the current window, we find that we must rebuild the heap by scratch for every window since we cannot selectively delete a value based on its index. This is clearly not ideal, so we want to devise a method that allows us optimal access to the largest value while also ensuring that that value is correct for the current window.  
If we keep removing items from a max heap, the value of those items will be given to us in descending order. As we want to preserve the positional information of elements (its index in `nums`) in the heap, we can pack an element's value along with its index in a tuple. Then the heap will present its elements based on the value, while allowing us to determine where in `nums` that element is stored in. While we cannot remove items from the heap based on its index, we can now determine whether an element popped off the heap belongs in the window or not by simply examining its index. We want the **largest** value within the current window, the heap gives us elements in decreasing order, and we know if an element from the heap is contained within the window or not. As such, we simply keep popping elements off of the heap until we encounter an element that is contained in the current window, which is appended to the return list. We then advance the window and add the newly included element to the heap.  

#### Conclusion
This solution takes $O(n\log n)$ time to run. We iterate along `nums`, while adding and removing items to a heap. Insertions and removals from the heap takes $O(\log k)$ time where $k$ is the size of the heap. The heap can grow to a size of $O(n)$ but each element in `nums` can be inserted and/or removed from the heap at most only once. The space complexity is $O(n)$.  
  

