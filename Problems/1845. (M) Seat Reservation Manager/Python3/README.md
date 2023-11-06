## 1845. (M) Seat Reservation Manager

### `solution.py`
We are only interested in reserving the seat with the smallest number at any given time, and as such we should be using a min heap as the underlying data structure. When `SeatManager` is initialized, we create a list containing all integers from `1` to `n`. That list is then turned into a heap using the built-in function `heapq.heapify()`. For calls to `reserve()`, we simply pop an element from the heap which is then immediately returned. When `unreserve(i)` is called, we simply push the integer `i` back onto the heap. For both `reserve()` and `unreserve(i)`, additional safety checks are not necessary as it is guaranteed that `reserve()` and `unreserve(i)` will be called 'correctly'.  

#### Conclusion
The initialization of `SeatManager` takes $O(n)$ time to perform, where $n$ is `n`. `heapq.heapify()` performs an in-place heapify which has a time complexity of $O(n)$. The space complexity of `SeatManager` is also $O(n)$, as the heap may contain as many as $n$ integers.  
Calls to `reserve()` and `unreserve()` will take $O(\log n)$ time to perform, as both methods perform a single pop/push operation on the heap whenever they are called. Their space complexity is $O(1)$, as heap pop/push operations do not require extra memory.  
  

### `solution_2.py`
The first solution works just fine, but the front-loaded time complexity could be considered bad behavior. Instead of instantiating a full heap of `n` seats during initialization, we can keep track of the smallest seat number that has *not been reserved yet*. As we want to reserve seats in ascending order of their numbers, we can simply return the smallest integer that has not yet been inserted into the heap, if the heap is empty. We then increment that value by `1`, and repeat the process whenever `reserve()` is called. Now we can initialize `SeatManager` with only an empty list and an integer, instead of heapifying a list of length `n`. The behavior of `unreserve(i)` is identical to the previous solution.  

#### Conclusion
The instantiation of `SeatManager` now only takes $O(1)$ time, as we only have to initialize an empty list and an integer. The overall space complexity is still $O(n)$.  
`reserve()` and `unreserve()` have the same time and space complexities as the previous implementation. `reserve()` however will now have a best case time complexity of $O(1)$, when the internal heap is empty.  

