## 1404. (M) Number of Steps to Reduce a Number in Binary Representation to One

### `solution.py`
Since the algorithm the problem describes is deterministic, and it is guaranteed that the value represented by `s` will eventually become `1`, the only hard part of this problem is converting the string `s` to an integer. Thankfully, Python trivializes this step by allowing us to specify which base a string should be interpreted as. Once `s` is converted into an integer, we simply apply the appropriate action based on the current value until it becomes `1`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. Converting `s` into an integer takes $O(n)$ time. Modifying the converted value until it becomes `1` takes $O(\log n)$ time as the value is halved whenever it is even. The space complexity is $O(1)$.  
  

