## 2336. (M) Smallest Number in Infinite Set

### `solution.py`
Since we only want the smallest value every time we pop from the 'infinite' set of integers, this set can be represented with a single integer that we increment every time an item is popped. Integers added with `addBack()` can be stored in a min heap, which gives us constant time access to the smallest value. However, since Python heap queues allow for non-unique values to be pushed we need to keep track of all items that have been pushed into the heap queue. We may use a set to record these integers since we can check whether a number is in a set or not in constant time.  
Now that we have figured out which data structures we should use internally, the implementation itself is relatively simple.  

#### Conclusion
Calls to `popSmallest()` will take $O(\log n)$ time to run, where $n$ is the number of calls made to `addBack()` (the size of the heap queue). Calls to `addBack()` will also take $O(\log n)$ time. The overall space complexity is $O(n)$ since the heap queue is the only object that fluctuates in size and can at most contain $n$ integers.  
  

