## 1751. (H) Maximum Number of Events That Can Be Attended II

### `solution.py`
First off, we can see that `events` is not sorted, which means that whenever we decide to attend an event we will need to scan through the entierety of `events` in order to identify events that do not conflict. Thus we can save time by sorting `events` by the starting date beforehand. Now, whenever we decide to attend an event we can use binary search to find the earliest event we can attend based on the current event's end date.  
We have established that we should be sorting `events` before doing anything, but how should we proceed after that? Well, we know that we want the maximum value after attending `k` events among the entirety of `events`. Could we come up with a state that the current one depends on? Let's say we are considering the leftmost event of the current state - which would be the `0`th event in the list of sorted events `ev_sorted`. We have two choices we can make, which are either attending the event or ignoring it to attend the next upcoming event. If we attend the current event, we will accrue the value assigned to it but cannot attend any events that conflicts with the current one. Since `ev_sorted` is already sorted in ascending order, we can find the first attendable event at index `nxt` by using binary search as we mentioned earlier. On top of this, we are only allowed to attend `k` events, and as such we can now attend `k-1` events. Putting these together we now know that the total value of attending the current event is `ev_sorted[0][2] + f(nxt, k-1)`, where `f(i, j)` is a function that returns the total maximum value when we can attend `j` events from `ev_sorted[i:]`. For the other choice where we ignore the current event, the value is simply `f(0+1, k)`. Whichever choice that yields the largest value is the optimal one, and so the complete function would look something like this: $f(i,j) = \text{max}(\texttt{ev_sorted}[i][2]+f(nxt,j-1), f(i+1,j))$. The base case is when $i$ is equal to `len(ev_sorted)` and when `k` is equal to `0`. Because $f$ may be called with the same parameters multiple times, we memoize the results in a $k \times \text{len}(\texttt{ev_sorted})$ 2D list.  
The value we want will be the return value of $f(0, k)$, which we can return as-is.  
  

#### Conclusion
The time complexity of this solution is $O(kn\log n)$, where $k$ is `k` and $n$ is the length of `events`. Sorting `events` takes $O(n\log n)$ time, and we fill in `dp` which is a $k\times n$ 2D list. For each value of `dp`, we perform a binary search on `ev_sorted` which is $n$ long, thus taking $O(\log n)$ time per value. The space complexity is $O(kn)$. `dp` uses $O(kn)$ space, and the recursion stack for $f$ can at most be $O(k+n)$ deep since either $i$ can be incremented by $1$ or $j$ can be decremented by $1$.  