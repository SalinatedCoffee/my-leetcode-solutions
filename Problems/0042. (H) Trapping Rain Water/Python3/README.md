## 42. (H) Trapping Rain Water

### `solution.py`
In order for water to be trapped above a column, there must be other columns on either side of it that are taller. As the 'area' of the trapped water can be any shape, it will be difficult to compute the amount of water as a whole. Instead, we can incrementally compute the total amount by calculating the amount of water trapped above each 'column'. For some column `i`, if we know the tallest column to either side of it *including itself*(largest value in `height[:i+1]` and `height[i:]`) we can trivially compute the amount of water trapped above it by selecting the smallest of the two columns and subtracting `height[i]` from it. This allows us to avoid any explicit checks that determine whether the two columns are taller than `height[i]`, since if either one(or both) of the two columns are shorter, this formula yields a value of `0`, which is what we want.  
We first initizlize 2 lists of length `len(height)` with the value of `0`. One will store the height of the tallest column towards the left of each column, and the other the column towards the right. Populating each list will require a single pass over `height`, once from left to right, and another from right to left. Once both lists are populated we make one last pass over `height`, using the formula described previously to compute the amount of water trapped over each column of `height`. This value is added to the running total `ret`, which is returned after all columns of `height` has been examined.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `height`. `height` is iterated over 3 times; once to populate `l`, once to populate `r`, and once to compute the total amount of trapped water. Each traversal takes $O(n)$ time, bringing the overall time complexity to $O(3n) = O(n)$. The space complexity is also $O(n)$, as the lists `l` and `r` are both $n$ long.  
  

