## 2191. (M) Sort the Jumbled Numbers

### `solution.py`
The list of integers `mapping` maps base 10 digits to a different digit. That is, if `mapping[i] = j` all digits `i` will be replaced with the digit `j`. For example, when `mapping = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]` the number `103` will be converted to `013 = 13`. Using `mapping`, we are asked to sort the list of integers `nums` in ascending order of the mapped value of each element. If two elements have the same mapped value, their relative order should be preserved. We can easily solve this problem by sorting `nums` using a custom comparator. Since Python's built in sort is guaranteed to be stable, we know that the ordering of identical values will be preserved after the sort.  
The problem now becomes implementing the comparator. We want to be able to swap out a digit of a number with a different digit, and we also need to be able to handle leading zeros. To do this, we can simply convert the number into a string, convert it into a digit string using `mapping`, and then convert it back into an integer. This can be achieved through a series of list comprehensions and a single lambda, the entirety of which can be encapsulated by yet another lambda so that it can be used as a custom comparator.  

#### Conclusion
This solution has a time complexity of $O(kn\log n)$, where $k$ is the average number of digits of the elements in `nums`, and $n$ the length of `nums`. Converting a number with $k$ digits using `mapping` takes $O(k)$ time, which is performed every time the value of a number needs to be compared by Python's sorting algorithm. Since the time complexity of said algorithm is $O(n\log n)$ on a list with size $n$, the overall time complexity of this solution becomes $O(kn\log n)$. The space complexity is $O(n)$, due to the sorting step.  
  

