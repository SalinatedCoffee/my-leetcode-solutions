## 852. (M) Peak Index in a Mountain Array

### `solution.py`
The linear time solution is trivial to implement, since we simply need to scan through `arr` until we find an element that is smaller than the one that immediately precedes it. A logarithmic solution however, is trickier to implement. First off, the problem involves searching an array for some value, and the elements are in sorted order. This tells us that we should be taking a binary search approach to this problem, especially so as the problem is asking us for a logarithmic solution. However the original solution only examines the single element at the center of the current interval, which is not enough information when choosing which half to take.  
Due to how the 'peak' is defined, `arr` is guaranteed to contain *exactly* one peak value. That is, `arr` can be split into two halves around the peak, where the first half monotonically increases and the second half monotonically decreases. Thus, if the 'slope' about an element is positive, it means that the element is in the first half and the peak is on the right side of that element - and vice versa. Now that we have found a criteria on which to base our decisions on we can implement the actual solution using binary search.    

#### Conclusion
This solution has a time complexity of $O(\log n)$ where $n$ is the length of `arr`. We binary search through `arr`, which continually reduces the search space in half until the desired value is found. The space complexity is $O(1)$.  
  

