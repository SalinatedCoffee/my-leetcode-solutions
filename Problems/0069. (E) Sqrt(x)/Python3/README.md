## 69. (E) Sqrt(x)

### `solution.py`
`x` is an unsigned 32-bit integer, and so we may simply try all roots in range `[1:31]`. The solution increments `i` by 1 and exits the loop whenever `x <= i*i`.  

#### Conclusion
The solution runs in $O(\log n)$ time and uses $O(1)$ space.  
  

### `solution_2.py`
As expected for a fundamental problem like this, there are many discrete algorithms that attempt to calculate the square root of a number to various precision. One such algorithm is the [Newton-Rhapson method](https://en.wikipedia.org/wiki/Newton%27s_method#Square_root), which is trivial to implement in code.  

#### Conclusion
The time complexity is $O(\log n)$, and the space complexity is $O(1)$.  
  

