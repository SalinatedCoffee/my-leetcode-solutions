## 1637. (M) Widest Vertical Area Between Two Points Containing No Points

### `solution.py`
While the wording of the problem is slightly confusing, it simply boils down to finding the largest distance between two adjacent points with respect to the x-axis. In order to easily access two such points we can sort `points` using the x-coordinates as the key. Now, if two points are adjacent in `points` it is also guaranteed that they are adjacent on the x-axis as well. We simply iterate over the sorted `points` and find the largest distance between two adjacent elements.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `points`. Python's `list.sort()` takes $O(n\log n)$ time to perform, which outscales the time it takes to iterate over the list ($O(n)$). The space complexity is $O(n)$, also due to the sorting step.  
  

