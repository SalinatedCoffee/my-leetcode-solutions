## 191. (E) Number of 1 Bits

### `solution.py`
This is a trivial problem to anyone with some knowledge about how integers are represented in binary and basic bitwise operations. We simply extract the LSB by bitwise-ANDing it with `1`, and bitshift `n` by 1 bit towards the left. If the LSB is `1`, we increment a counter by `1`. We repeat these steps until `n` is `0`, after which we return the counter.  

#### Conclusion
The time complexity of this solution is $O(\log n)$, where $n$ is `n`. Each time we bitshift `n` towards the left, we are essentially halving `n` - which is why the `while` loop will run at most $\log n$ times. The space complexity is $O(1)$.  
  

