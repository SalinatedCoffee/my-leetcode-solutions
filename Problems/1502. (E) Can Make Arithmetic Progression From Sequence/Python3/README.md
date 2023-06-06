## 1502. (E) Can Make Arithmetic Progression From Sequence

### `solution.py`

The given list is not sorted, and so we would have to iterate across the entire list in order to find the preceding and succeeding element for any given value. Instead, we may sort the list beforehand which allows us to simply iterate along the list while comparing neighboring elements.  



#### Conclusion

This solution has a time complexity of $O(n\log n)$, where $n$ is the number of elements in the sequence. The space complexity is $O(n)$, since the sorting step uses $O(n)$ memory during runtime.  


