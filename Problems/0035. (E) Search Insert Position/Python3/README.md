## 35. (E) Search Insert Position

### `solution.py`
A simple iterative solution could have worked, but the problem specifically says to write a solution that runs in logarithmic time which means we must use binary search. We immediately return if we find `target` or return `lo` after the `while` loop as we want the position of where `target` would have existed had it been in `nums`.  
Don't forget to perturb `mid` by 1 as there is no point in looking at `nums[mid]` in the next iteration of the loop, and to avoid infinite loops.  
  
#### Conclusion
This solution takes $O(\log n)$ time to run as it splits the input list by half every iteration until it either finds `target` or the list can not be split any further. It has a space complexity of $O(1)$ as it is an iterative solution that uses a fixed amount of memory. A recursive solution would have had a space complexity of $O(\log n)$ due to the recursion stack.  
  
