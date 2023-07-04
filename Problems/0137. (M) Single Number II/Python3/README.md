## 137. (M) Single Number II

### `solution.py`
The XOR trick unfortunately will not work here, since we are dealing with triples of integers rather than pairs. Thus, we need to count the number of set bits for each binary digit and reconstruct the singular number from those values. Since we are working in Python, we cannot bit shift the values in `nums` because it may contain negative numbers. Instead we have to create a mask and bit shift it instead to extract a set bit. If a bit is set we increment the corresponding counter in `bits`. Once we have finished iterating over `nums`, we now iterate over `bits` and see whether a value can be divisible by 3. If yes, it means that the singular number does not have that bit set and we do nothing. If not we do the opposite by setting the bit for that specific binary digit. Due to the way Python handles negative numbers and right bitshift operations, we need to manually check whether the sign bit is set and modify the return value accordingly.  

#### Conclusion
As required by the problem, this solution has a time complexity of $O(32n) = O(n)$ where $n$ is the length of `nums`. The space complexity is $O(32) = O(1)$.  
  

