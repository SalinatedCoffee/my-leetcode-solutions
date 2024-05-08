## 506. (E) Relative Ranks

### `solution.py`
As we essentially want to 'swap out' each value in `score` with their rank, we should find a way to sort the index of each value according to their size. This can be easily achieved through a variety of means, but here we have opted to create a new list with tuples containing the value and its index, and sorting it in-place. The elements of `score` can now be accessed in order of their values, which we can use to populate the return list `ret` with the appropriate string.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `score`. Creating a new list that includes the index of each value in `score` takes $O(n)$ time, and sorting that list using Python's built-in sort takes $O(n\log n)$ time. The space complexity is $O(n)$, due to both the list `score_sorted` and sorting said list in-place.  
  

