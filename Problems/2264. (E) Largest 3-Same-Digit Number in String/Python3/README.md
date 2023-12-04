## 2264. (E) Largest 3-Same-Digit Number in String

### `solution.py`
For this problem, we obviously have to examine the entirety of `num`. We iterate along `num` from left to right, and keep track of the number of consecutive identical digits. Whenever this number is `3`, we update the largest digit `d` if needed. As the ASCII codes for characters `0` through `9` are conveniently ordered the same, we can simply use `max()` to update `d`.  
Once the iteration completes, we return `d*3` as the problem requires us to return a string representation of the number.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `num`. We examine every character of `num`, with each of them taking constant time to process. The space complexity is $O(1)$.  
  

