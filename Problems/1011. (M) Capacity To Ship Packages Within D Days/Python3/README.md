## 1011. (M) Capacity To Ship Packages Within D Days

### `solution.py`
My first instinct was to try the capacity of all 'prefix' subarrays and choosing the smallest capacity (dynamic programming). There was however one big problem with this method, which was that the capacity depends on the size of the packages (ex. for packages `[2, 2, 2]` the potential capacity can only increase by 2). So I moved on to a somewhat brute force-'ish' approach which is trying all valid capacities in a binary search fashion. The idea is to set an initial capacity range and try shipping the packages with a capacity that is the middle of that range and so on, so forth. In this case the initial range would be `[max(weights), sum(weights)]` since the minimum capacity has to be at least the weight of the largest package for it to be potentially valid, and the largest is a capacity that can store all packages at once. We then implement `valid(cap)` that checks whether the packages are shippable within the given time limit and capacity `cap`. If a 'midpoint' capacity is determined to be valid, it means that a lower capacity may also be valid and thus we choose the left half for the next iteration.  

#### Conclusion
This solution runs in $O(n\log n)$ time as `valid()` takes $O(n)$ time to run and is evaluated $\log n$ times. The space complexity is $O(1)$.  
  

