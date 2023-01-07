## 134. (M) Gas Station

### `solution.py`
Perhaps the easiest way is attempting a brute force approach where we try every station until we find a solution. This solution while technically correct(as in it will *eventually* find the correct solution), is horribly inefficient and TLEs some testcases.  
  
#### Conclusion
The time complexity of this solution is $O(n^2)$ since in the worst case, all starting stations($n$) will fail right before making the last trip($n$). The space complexity is $O(1)$ because `range()` in Python 3 uses an iterator instead of generating a list.  
  

### `solution_2.py`
So the brute force solution works, but it isn't fast enough. Exploring other options, we notice that we can verify whether a solution exists by simply subtracting the total cost from the total fuel. If the value is negative a solution does not exist and vice versa. This can be computed in linear time, but we still need to find the starting index.To accomplish this, we'll make our fuel tank magical and let it contain *negative* amounts of fuel. By doing this we can quickly see that whenever the total fuel minus the total cost drops below zero we can just abandon that interval and start a fresh run. Consider a situation where there are a series of stations preceding an unreachable station. No matter which station we start from, as long as the station belongs in that series we cannot possibly travel to the unreachable station(and by extension, travel through all stations). Thus we can safely disregard the previous stations (by resetting the fuel tank), record the start of the new string of stations, and try starting from the next station in the list.  
Now we have the starting position of a sequence of traversable stations (that ends with the end of the given lists), but we're still not sure if we can travel through all stations after wrapping around to the start of the station list. We *could* do a second pass, and that will still be decently faster than the previous solution. But we can avoid skipping one more time by looking at the total remaining fuel (`sum(fuel)-sum(cost)`). If this value is negative, a solution cannot possibly exist since fuel expenditure is larger than the fuel provided. If this value is larger than or equal to 0, a solution exists and it is *guaranteed to be unique* according to the problem description. And since we have already established that the starting station cannot exist before the recorded position, we can just check the remainder of the total fuel and return a value accordingly.  
  
#### Conclusion
This solution runs in $O(n)$ time and also uses $O(1)$ space.  
Admittedly I'm quite bad with words and the explanation turned out to be a bit longer than I would have liked. But in essence this solution is just a sub-variant of [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem#Kadane's_algorithm).
  
