## 2864. (E) Maximum Odd Binary Number

### `solution.py`
In order for a binary number to be odd, the least significant bit must be raised. Since `s` is guaranteed to contain at least 1 `1`, and we are allowed to return a binary number with leading zeros, we can simply count the number of raised bits in `s` and use that to construct the desired string. The string consists of three parts; a run of `1`s, a run of `0`s, and a single `1`. Because we are asked to return the largest number we would obviously want to push all available `1`s to the most significant digits possible. If the number of `1`s in `s` is `pop`, the length of these sections should be `pop - 1`, `len(s) - pop`, and `1`, respectively.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. `s` is iterated over once in order to count the number of raised bits, hence the overall time complexity. The space complexity is $O(1)$, excluding the memory used by the string being returned.  
  

