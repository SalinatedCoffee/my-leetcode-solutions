## 1523. (E) Count Odd Numbers in an Interval Range

### `solution.py`
We immediately realize that we can simple take the difference between `low` and `high` and divide by 2 to get the desired number. However we must also account for when the bounds are odd, and after checking a few examples (which is perfectly practical since we only have 4 cases to consider) we see that we should increment the aforementioned number by 1 whenever `low` or `high` are odd.  
A slightly more analytical approach can be found in the [official solution](https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/solutions/2957338/count-odd-numbers-in-an-interval-range/).  

#### Conclusion
The solution has a time and space complexity of $O(1)$.  
You could replace the modulo operations with bitwise ones to get even better performance.  

