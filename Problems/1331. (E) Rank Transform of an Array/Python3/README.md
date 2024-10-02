## 1331. (E) Rank Transform of an Array

### `solution.py`
Given the array of integers `arr`, we are asked to return a list of their corresponding ranks. Rank starts at `1`, and corresponds to an element's relative size within `arr`. Larger values should be ranked higher, and equal values should be assigned the same rank. Rank should also be assigned 'densely', in the sense that the number of unique values in `arr` should be equal to the rank of the largest value.  
As we want to effectively order the unique values in `arr` in ascending order, we would want to first reduce `arr` to its unique elements and then sort them. The former can be accomplished using a set, and Python's built in sort can be used to achieve the latter. The index of each value in the sorted list + 1 is the rank of that unique value, but we need to be able to map a unique value to its rank which we cannot do given the current list. Converting the list into a dictionary using the unique element as the key and its index in the sorted list as the value, we can now determine the rank given the value of an element in `arr`. All of these steps can be condensed into a single line through a combination of `map` and list comprehensions.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `arr`. The list of unique elements of `arr` can contain at most $n$ values, which requires $O(n\log n)$ time to sort using Python's built in sort. Generating the list of ranks takes $O(n)$ time. The space complexity is $O(n)$ due to the sorting step as well as the list of unique elements of `arr`, which is kept in memory until the algorithm exits.  
  

