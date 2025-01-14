## 2657. (M) Find the Prefix Common Array of Two Arrays

### `solution.py`
The lists of integers `A` and `B` are permutations of the integers in the range `[1, len(A)]`. We are asked to return the prefix common array of `A` and `B`, where a prefix common array `C` is a list of integers where `C[i]` is equal to the count of numbers that are present in *both* `A[:i+1]` and `B[:i+1]`.  
Because the constraints on both lists are small, a brute force approach may work for this problem. However, it is not that difficult to see that we could do much better than that. Since both lists are *permutations* of integers in a fixed interval, we know that a value will appear exactly twice - once in each list. Using this property, we can use a set to store previously seen values, and a counter that keeps track of the number of values that have appeared in both lists. Iterating over both lists simultaneously, we first check if the current value is already in the set. If not, we simply add the value to the set. Otherwise, we remove the value from the set and increment the counter by `1`. After processing the elements from both lists, we add the current counter to the prefix common array.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `A`(and also `B`). Both lists are simultaneously iterated over exactly once, with each element requiring $O(1)$ time to process. Thus, the overall time complexity of this solution is $O(n)$. The space complexity is also $O(n)$, due to the set `freq`.  
  

