## 119. (E) Pascal's Triangle II

### `solution.py`
The trivial solution is exactly the same as problem [118, Pascal's Triangle](..%2F..%2F0118.%20%28E%29%20Pascal%27s%20Triangle), with the minor difference being that the given row number is 0-indexed.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is `rowIndex`. The space complexity is also $O(n^2)$.  
  

### `solution_2.py`
The follow-up asks us to implement a solution that uses $O(n)$ space, which we can trivially do by only keeping the previously computed row in memory. The previous row is stored in `prev`, which is replaced with the current row `c_row` after the entierety of `c_row` has been computed.  

#### Conclusion
The time complexity of this solution is $O(n^2)$, and the space complexity is $O(n)$.  
  
