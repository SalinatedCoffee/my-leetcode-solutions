## 2610. (M) Convert an Array Into a 2D Array With Conditions

### `solution.py`
The problem is essentially asking us to partition `nums` into arrays that each only contain unique values. There are many ways to approach this problem, but here we will use a dictionary (more specifically, Python's `Counter` objects). If we keep a counter for each unique value in `nums`, we can easily partition `nums` in the desired configuration. We initialize a `Counter` object passing `nums` as the argument, which will populate a dictionary with each unique values of `nums` as the key and the number of its appearences in `nums` as the value. The counter is then iterated over, checking the value of each key. If the value is non-zero, we add the corresponding key to a list, then decrement the value by `1`. Otherwise, we simply skip over it. Once all key-value pairs have been examined, we append the current list of keys to another list, and repeat these steps until all values in the counter are `0`. We then return the 2D list of keys, which will meet the requirements described in the problem.  

#### Conclusion
The time complexity is $O(n)$, where $n$ is the length of `nums`. Instantiating the counter takes $O(n)$ time, as well as the partitioning step. The space complexity is also $O(n)$, as the counter `freq` can contain at most $n$ key-value pairs.  
  

