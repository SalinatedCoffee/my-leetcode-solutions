## 1460. (E) Make Two Arrays Equal by Reversing Subarrays

### `solution.py`
Given 2 lists of integers with equal length `target` and `arr`, we are asked to determine whether reversing subarrays of `arr` can make its contents identical to that of `target`. If `target` contains a value that is not in `arr`, it is obviously impossible to make `arr` identical to `target`. If the two arrays contain the same set of values but in different order, how can we verify whether `arr` can be reordered to match that of `target`? The problem says that we can only reverse non-empty subarrays in `arr` an unlimited number of times. This essentially means that we can order the elements in `arr` however we want. Consider the list `[2, 3, 4, 1]`, for example. If we wanted to move the `1` to become the `0`th item in the list, we can first swap the `4` and `1` to get the list `[2, 3, 1, 4]`. The `1` can then be swapped with `3` and then with `2` to get the list `[1, 2, 3, 4]`, which is what we wanted. Thus, by chaining swaps of two adjacent values we can put the contents of `arr` in any order, and the problem now becomes comparing the frequency of each unique element in `target` and `arr`. If all of them are equal it means that `arr` can indeed be reordered to match that of `target`. If not, reordering is impossible and we return `False`. The frequency of unique elements can be easily generated ba a Python `Counter`, which has the added bonus of supporting the `==` operator between `Counter`s. The expression returns `True` if all *key-value pairs* match, which is exactly what we want.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `target`. Generating the frequency list of the two lists takes $O(n)$ time to complete, as well as the comparison operation between the `Counter` of each list. The space complexity is also $O(n)$, due to the use of `Counter`s.  
  
