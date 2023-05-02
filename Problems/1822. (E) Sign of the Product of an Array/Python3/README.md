## 1822. (E) Sign of the Product of an Array

### `solution.py`
We only want the sign of the product, so we can ignore the actual value. Multiplying positive values does not change the sign, and multiplying a negative value with a positive one will flip the sign. Using this property, we can simply count the number of negative values and then determine the final sign. The implemented solution uses bitwise operators instead for a small performance increase.  
When a zero is encountered we may return `0` immediately as any number multiplied by zero will always be zero.  

#### Conclusion
The solution runs in $O(n)$ time where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

