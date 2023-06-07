## 1318. (M) Minimum Flips to Make a OR b Equal to c

### `solution.py`

We can simply iterate over the binary representations of the three integers while incrementing a counter when appropriate. Deciding whether to flip a bit at some digit does not depend on any others, which means there is no need to use dynamic programming. At a digit then, there are two scenarios; the digit of `c` can either be a `0` or `1`. For the former, both digits of `a` and `b` need to be `0` and thus we increment the counter for each `1` we find. For the latter any bit from `a` or `b` needs to be `1`, so we only increment the counter when **both** bits are `0`.  

All three integers are bit-shifted to the right by 1 every iteration. When all three integers are `0`, we may exit the while loop and return the value of the counter.  

#### Conclusion

The time complexity of this solution is $O(\text{max}(\log(a), \log(b), \log(c))$ where $a$, $b$, and $c$ are the input integers `a`, `b`, and `c`, respectively. The loop continues until all integers are `0`, and the integers are bit-shifted by 1 towards the right each iteration. Bit-shifting by 1 to the right essentially halves an integer in base 10, hence the logarithmic running time. The space complexity is $O(1)$.  
