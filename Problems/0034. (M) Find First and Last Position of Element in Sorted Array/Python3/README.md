## 34. (M) Find First and Last Position of Element in Sorted Array

### `solution.py`
We are dealing with sorted arrays, and the problem requires us to come up with a solution that runs in $O(\log n)$ time - which are unmistakable signs of a binary search solution. Instead of searching for a single match however, we would need to modify the search criteria slightly in order to find the indices of the first and last occurance of `target` in `nums`, if they exist.  
A simple solution is to simply run binary search twice; once to find the first element, and once to find the last element. When searching for the first element, we know that we should select the left half whenever the middle element equals `target`. This is also the case when the pivot is larger than `target`. When searching for the last element, we should be selecting the right half when the pivot is equal to `target`, as well as when it is smaller than `target`. In both cases, we update the last index seen whenever it is determined that the pivot `nums[m] == target`.  
If `target` does not exist in `nums`, the indices will never be touched and will keep their initialized value. When this is the case, we simply return `[-1, -1]`.  

#### Conclusion
This solution has a time complexity of $O(\log n)$, where $n$ is the length of `nums`. Binary search is performed twice on `nums`, with only a fixed number of constant-time operations being performed for each iteration. The space complexity is $O(1)$.  


### `solution_2.py`
With the binary search implemented in the previous solution, we have basically impelemented Python's `bisect.bisect_left()` and `bisect.bisect_right()`. These can be used as near drop-in replacements, with the sole difference is that these functions will return the position of where an element should be *inserted*. For example, if `nums = [1, 2, 5]` and `target = 3`, these functions will both return `2`. Hence, we implicitly check for this case by subtracting `1` from the index of the 'last' element `r` and returning `[-1, -1]` if `l > r`.  

#### Conclusion
The time and space complexity for this solution is identical to the first.  
