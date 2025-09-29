## 976. (E) Largest Perimeter Triangle

### `solution.py`
Given the list of edge lengths `nums`, we are asked to return the longest perimeter of a triangle with a non-zero area that can be formed using the edges in `nums`. For a valid triangle (triangle with a non-zero area) to be formed, the edge lengths $a$, $b$, and $c$ must satisfy the expression $a + b > c$, where $a \leq b \leq c$. Say we already know what the value of $c$ is. Since we want the largest possible perimeter of a valid triangle, we would want to select the largest possible values for $a$ and $b$ among the remaining edges. In other words, we want the first and second largest values smaller than $c$. If we sort `nums`, these two values can be trivially identified for any given value for $c$.  
`nums` is first sorted in ascending order. We then iterate along the sorted list starting with the largest 3 values. If a valid triangle can be formed using the three values, we immediately return their sum. Otherwise, we try the next set of values until we find a set that forms a valid triangle. If the loop exits, a valid triangle cannot be formed using any combination of the edges given in `nums`, and we simply return `0`.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ , where $n$ is the length of `nums`. Sorting `nums` with Python's built-in `.sort()` method finishes in $O(n\log n)$ time. `nums` is iterated over afterwards, which takes $O(n)$ time to run. Therefore, the overall time complexity of this solution is $O(n\log n)$. The space complexity is $O(n)$, due to the sorting step.  
  

