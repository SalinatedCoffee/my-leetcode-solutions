## 1296. (M) Divide Array in Sets of K Consecutive Numbers

### `solution.py`
This problem is exactly the same as [problem 846, Hand of Straights](../../0846.%20%28M%29%20Hand%20of%20Straights). Essentially, because we want to group the values in `nums` in consecutive values, we can greedily match unique values if we do so in order. The number of occurances of each unique value is first counted using a Python `Counter`, after which the list of unique values is sorted in ascending order. This list is then iterated over, while attempting to match the unique value `i` with the other values in its group. If at any point there are more values `i` than there are `i+j` where `i < j < k`, `nums` *cannot* be grouped into groups of `k` and we can immediately return `False`. Otherwise the iteration over the sorted list of keys will exit normally, at which point we can return `True`.  

#### Conclusion
This solution has a time complexity of $O(nk+n\log n+n)$ where $n$ is the length of `nums` and $k$ is `k`. The space complexity is $O(n)$.  
  

