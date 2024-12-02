## 1346. (E) Check If N and Its Double Exist

### `solution.py`
Given the array of integers `arr`, we are asked to determine whether a pair of elements `arr[i]`, `arr[j]` exist such that `i != j` and `arr[i] * 2 == arr[j]`. Because we know which value to look for when given some element in `arr`, we can simply store the elements of `arr` in a dictionary so that we may determine an existence of a value in constant time. One thing to note here is that `arr` may contain `0` and a pair must not consist of the same element. This means we also need to know how many of each unique value exists in `nums` in order to handle the edge case where `arr` contains(among other values) a single `0`. Python's `Counter`s are an easy fix to this problem, using each unique value as the key and the value's frequency in `arr` as the value. `arr` is then iterated over while checking whether the double of the current element exists in `arr`, or more than 2 of the current element exists if it is `0`.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `arr`. Initializing a `Counter` using the contents of `arr` requires $O(n)$ time to complete, as well as iterating over `arr` while searching for a valid pair. The space complexity is also $O(n)$, due to the dictionary `nums`.  
  

