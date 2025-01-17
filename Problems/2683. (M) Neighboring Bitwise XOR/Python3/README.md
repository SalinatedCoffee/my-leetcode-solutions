## 2683. (M) Neighboring Bitwise XOR

### `solution.py`
The binary list `derived` is a list of values resulting from XORing adjacent pairs of values in some original list. If we call this list `original`, the value of `derived[i]` would be the value of `original[i] ^ original[i+1]`. If `i == len(original)-1`, `derived[i]` would be equal to `original[i] ^ original[0]`. Our task is to determine whether `original` can exist given the values in `derived`.  
Thinking about the problem, we observe that some value `original[i]` will be XORed exactly twice. Once to compute `derived[i-1]`, and once to compute `derived[i]`. Since XORing a value with itself results in a value of `0`, we know that if we were to XOR `derived[i-1]` and `derived[i]`, `original[i]` will become `0`. The expanded expression is `original[i-1] ^ original[i] ^ original[i] ^ original[i+1] == original[i-1] ^ original[i+1]`. But, since `original[i-1]` and `original[i+1]` are each XORed once more also, they will be come `0` as well. In fact, since `derived` is generated circularly(`derived[len(original)]`), *each and every* element in `original` will be XORed exactly twice. Thus, if we compute the XOR sum of `derived`, the resulting value should be `0` if it can be generated from a binary list of the same length.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `derived`. The space complexity is $O(1)$.  
  

