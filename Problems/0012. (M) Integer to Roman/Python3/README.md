## 12. (M) Integer to Roman

### `solution.py`
We immediately realize that we can implement a greedy algorithm to convert `num` to roman numerals. This is because we want to prioritize using the larger 'token's as much as possible when converting a value. For example, the correct roman numeral for `5` is simply `V`, instead of `IIIII` or `IVI`.  
Two arrays are initialized, where one holds the numeric value of each roman numeral and the other the string representation of said numerals. We then enter a while loop that continues until `num` becomes `0`. For each loop, we first find the largest numeral that is smaller than `num`. `num` is then decremented by the value of the numeral from the previous step, and the corresponding string representation is concatenated to the return string `ret`. These two steps are then repeated, after which we can simply return the completed numeral string.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is `num`. The space complexity is $O(1)$, as there are a fixed number of roman numerals that are kept in memory.  
  

