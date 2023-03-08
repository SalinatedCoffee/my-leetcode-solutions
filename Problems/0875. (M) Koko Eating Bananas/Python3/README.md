## 875. (M) Koko Eating Bananas

### `solution.py`
Before doing anything else we should first determine how we can compute the number of hours it would take to consume all bananas given some eating speed. This is rather simple since we can iterate through all piles and dividing by the eating speed and adding the ceiling of that value to a sum variable.  
Now we need to figure out a way to find the minimum eating rate, which we can do with binary search. The starting lower bound is trivially 1, and the upper bound is the largest value of `piles` since we can't consume multiple piles at once so we want the minimum rate at which we can consume any pile within 1 hour.  
Then the implementation itself is relatively simple, we simply need to remember to keep track of the last valid eating rate since we want to find the minimum speed instead of an exact match.  

#### Conclusion
This solution has a time complexity of $O(n\log m)$, where $n$ is the size of `piles` and $m$ is `h`. We use binary search, and for each iteration we iterate through `piles`. If $m$ has a fixed data type, the running time would technically be $O(n)$. The space complexity is $O(1)$ as no variables scale according to the input size.  
  
  
