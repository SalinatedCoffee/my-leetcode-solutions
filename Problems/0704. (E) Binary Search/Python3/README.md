## 704. (E) Binary Search

### `solution.py`
Binary Search is a classic search algorithm that can perform an efficient search on a sorted array. The algorithm splits an array in half and 'discards' one half by comparing the middle element against the item being searched. Assuming that the array is sorted in ascending order, if the median is larger than the search target, it means that the target is in the lower half and thus the upper half is discarded (WLOG for the opposite case). This way, the search can be performed in logarithmic time instead of linear time.  
If the split halves are empty, then we return `-1` since the search term does not exist in the array.  

#### Conclusion
The time complexity is $O(\log n)$, where $n$ is the size of `nums`. The space complexity is $O(1)$.  
  

