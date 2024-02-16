## 1481. (M) Least Number of Unique Integers after K Removals

### `solution.py`
We want to remove elements of `arr` to reduce the number of unique integers in `arr`. Hence it would be reasonable to argue that we should be prioritizing values that appear less frequently in `arr`, since that would reduce the number of unique value by incurring less cost.  
A `Counter` is used to count the frequency of each unique value in `arr`, which is then converted to a list of key-value pairs and sorted by order of increasing value. The sorted list is then iterated over, while greedily 'removing' the unique values until we exhaust our deletion budget. Since we know the number of unique values that have been removed, we simply subtract this from the total number of unique elements in `arr`, and return it.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `arr`. While the counting step only requires $O(n)$ time to complete, the resulting key-value pairs are then sorted. If we look at the problem constraints, the range of $n$ is smaller than the range of `arr[i]`. Thus, we can argue that the sorting step has a worst-case time complexity of $O(n\log n)$, as the number of key-value pairs is bound by $n$. The space complexity is $O(n)$.  
  

