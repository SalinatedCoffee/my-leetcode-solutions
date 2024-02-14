## 2149. (M) Rearrange Array Elements by Sign

### `solution.py`
We are essentially being asked to first separate `nums` into 2 lists based on their signs, and then interleave the lists back into 1 starting where the first value is positive. One easy way to accomplish this is to do just that; separate the values of `nums` into 2 queues after which the queues are iterated over to generate the desired list.  

#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is the length of `nums`. Iterating over `nums` and interleaving the two queues each take $O(n)$ time. A single copy of each element in `nums` is kept in memory, hence the space complexity of $O(n)$.  
  


### `solution_2.py`
A better approach is to use 2 pointers instead of keeping the elements in memory. `pos` and `neg` point to the 'current' positive and negative elements in `nums`, respectively. We first append the item at `nums[pos]` to the return list, after which we advance `pos` incrementally until it points to another positive value. These steps are repeated for `neg` for negative values, after which we repeat until we reach the end of `nums`.  

#### Conclusion
This solution has a time complexity of $O(n)$ and a space complexity of $O(1)$.  
  

