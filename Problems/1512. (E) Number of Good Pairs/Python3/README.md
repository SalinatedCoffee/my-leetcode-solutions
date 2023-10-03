## 1512. (E) Number of Good Pairs

### `solution.py`
For a pair of numbers to be 'good', their values must be equal and the index of the first value must be smaller than the second value's. This essentially means that a pair can be considered good as long as it does not consist of the same instance in `nums`. As such, we only need to count the number of occurences of all values in `nums` after which we can easily compute the number of good pairs for each value.  
Say some number `i` appears 5 times in `nums`. If we sort the indices of each appearance in ascending order, it is easy to visualise that we can compute the total number of good pairs using the formula $n(n-1)/2$. In fact, we can simply skip the sorting step altogether as we only need the number of occurences of `i` but not the indices of each occurence in `nums`.  
As such, we simply instantiate a Python `Counter` (`i2i`) while providing `nums` as an argument. `i2i[i]` will be the number of occurences of the value `i` in `nums`. For all values in `i2i` we compute the number of good pairs and take the sum of all of these values, which can be returned directly.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of `nums`. It takes $O(n)$ time to process `nums` into `i2i`, and `i2i` can use $O(n)$ memory as the worst case is when `nums` contains no unique numbers.  
  

