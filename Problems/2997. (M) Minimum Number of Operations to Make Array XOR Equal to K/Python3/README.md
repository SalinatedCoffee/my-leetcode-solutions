## 2997. (M) Minimum Number of Operations to Make Array XOR Equal to K

### `solution.py`
At first glance it would seem that some kind of dynamic programming based approach would be called for. However, we can quickly see that there is no need to actually flip bits of the elements of `nums`. To flip a digit of the XOR sum, we only need flip a bit of a single element in `nums`.  
We first compute the XOR sum of `nums`. Then, we compare it against the target `k`, incrementing a counter `ret` by `1` whenever the digits do not match, necessitating a flip operation. We do this by extracting the LSB of each value and comparing them, after which we shift both values towards the right by 1 digit. When both the XOR sum and `k` become `0`, there are no more digits left to compare, and so we return `ret`.  

#### Conclusion
This solution has a time complexity of $O(n+\log(\max(\texttt{nums}, \texttt{k})))$, where $n$ is the length of `nums`. Computing the XOR sum of `nums` takes $O(n)$ time. The length of the XOR sum can at most be that of the binary length of the largest value in `nums`. Iterating over the digits is a linear time process, and since there are $\log(i)$ binary digits for an integer $i$, comparing the XOR sum and `k` will take logarithmic time of the larger of the two values. The space complexity is $O(1)$, as we only use a handful of fixed size variables.  
  

