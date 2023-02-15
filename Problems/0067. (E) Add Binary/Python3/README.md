## 67. (E) Add Binary

### `solution.py`
Given the constraints on the length of `a` and `b` we know that we cannot simply convert the strings to a number and add them. Thankfully implementing a linear time algorithm that adds the two strings without any type conversion is quite easy. We simply compute the sum of the previous carry and two digits (or one if `a` and `b` do not have the same length), append that sum modulo 2 to a result string, and of course update `carry` as necessary. After the addition is complete we need to look at `carry` one more time to check whether we need to append a `1` to the result string.  
Before returning, we also need to reverse the result string since it was generated LSB-first.  

#### Conclusion
The solution takes $O(n)$ time to run, where $n$ is equal to `max(len(a), len(b))`. It also uses $O(n)$ space since the length of the return string scales linearly with the length of the input strings.  
  
