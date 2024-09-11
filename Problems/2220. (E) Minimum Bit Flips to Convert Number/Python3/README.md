## 2220. (E) Minimum Bit Flips to Convert Number

### `solution.py`
Given the integers `start` and `goal`, we are asked to return the number of minimum bit flips required to convert the binary representation of `start` to that of `goal`. To convert `start` to `goal` using the smallest number of bit flips means that a bit that needs to be flipped is flipped only once, which consequently means that the number of bit flips is simply the number of differing bits between the two integers. We can produce a number that 'highlights' the differing bits by computing the XOR of the two integers, where a bit will be `1` if `start` and `goal` differed at that digit. After XORing the two values we can count the number of raised bits by masking out the LSB and shifting the value 1 bit towards the right until the value becomes `0`.  

#### Conclusion
This solution has a time complexity of $O(\log(\max(m, n)))$, where $m$ and $n$ are `start` and `goal`, respectively. XORing `start` and `goal` can be considered as taking $O(1)$ time to complete since the constraints on both inputs are small enough for them to be computed in a minimum number of CPU cycles. The counting of the raised bits after takes $O(\log(\max(m, n)))$ time, bringing the overall time complexity to $O(\log(\max(m, n)))$. The space complexity is $O(1)$.  
  

