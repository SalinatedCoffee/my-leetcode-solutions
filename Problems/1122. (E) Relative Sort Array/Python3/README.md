## 1122. (E) Relative Sort Array

### `solution.py`
Given 2 arrays `arr1` and `arr2`, we are asked to sort `arr1` based on the ordering defined by `arr2`. All elements in `arr2` are unique, and are guaranteed to exist in `arr1`. Elements in `arr1` may *not* exist in `arr2`, and these items should be appended to the end of the sorted list in ascending order of their values. This problem can be easily solved by using a dictionary, where we store the frequency count of each unique value in `arr1`. We can then iterate over `arr2`, looking up each element in the dictionary to incrementally create the sorted list of values. Once all elements in `arr2` have been examined, we sort the remaining values in `arr1`(or in this case, the remaining *unique* values) in ascending order and create the remainder of the sorted list.  

#### Conclusion
This solution has a time complexity of $O(m+n\log n)$ where $m$ is the length of `arr2` and $n$ is the length of `arr1`. Counting the unique elements of `arr1` takes $O(n)$ time. The initial sorting step takes $O(m)$ time as we iterate over `arr2` to retrieve each unique element in the provided order. Creating the remainder of the list takes $O(n\log n)$ time since there are $O(n)$ number of elements in `arr1` that do not exist in `arr2`. The space complexity is $O(n)$, due to the dictionary `arr1_freq` and the sorting step.  
  

