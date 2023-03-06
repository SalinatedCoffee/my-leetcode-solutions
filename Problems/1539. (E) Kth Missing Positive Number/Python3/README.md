## 1539. (E) Kth Missing Positive Number

### `solution.py`
A linear solution that simply counts the number of missing integers is trivial to implement. So instead we will take into account the follow-up question as well.  
We need to design an algorithm that runs in sub-linear time. In this context, we could use binary search to solve this problem as we want to find a single value given an array. But we're asked to find the K-th missing integer, instead of being given a specific value. What do we use as the criteria for our binary search?  
Given a value and the position of that value we can compute the number of missing integers up to the value in question. Suppose we have an array `[5]`. The element `5` has an index of `0` - which means that it is the first element in the array. To get the number of missing integers then we simply need to subtract the position of the element with its value; while also accounting for the fact that array indices are 0-indexed.  
Now we can implement a binary search that returns the index of the element before the first element that has the same or greater number of missing elements than `k`, and return that index + `k`.  
  
#### Conclusion
This solution runs in $O(\log n)$ time and uses $O(1)$ memory.  
  

