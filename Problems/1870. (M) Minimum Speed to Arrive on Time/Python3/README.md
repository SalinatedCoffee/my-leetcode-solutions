## 1870. (M) Minimum Speed to Arrive on Time

### `solution.py`

Before doing anything else we should first devise a method to verify whether `dist` is traversable given `hours` for some speed `s`. All trips depart exactly on top of the hour, and thus we need to wait for the next hour no matter how early we complete the previous trip. That is if we take a trip has a distance of `3` with speed `2`, it will take us `3 / 2 = 1.5` hours to complete it. However the next trip does not depart until hour `2`, and so we must add `0.5` hours to the trip duration. This is analogous to taking the ceiling of the trip duration. The last leg gets us to the destination, thus waiting is not necessary. Using this information we can see that the total time it would take to traverse `dist` with speed `s` can be calculated through the expression `sum([ceil(x/s) for x in dist[:-1]) + dist[-1]/s`. If this value is smaller than `hours`, `dist` is traversable with speed `s`.  
Now we need to figure out a way to search for the smallest speed that makes `dist` traversable within `hours`. There is no straightforward way of determining this mathematically through the values of `dist`, so it would seem that we would have to try various values for `s` until we find the smallest value that satisfies the condition. Thankfully `s` is an integer, and we know that its domain range is $[1, 10^7]$, and thus it stands to reason that we could use binary search on `s` and achieve reasonable time complexity.  
There are two details that should be considered in the implementation of the solution; realizing when a solution does not exist, and how to store the return value. From the validation expression described earlier we can say that if there are more trips than the number of hours, a solution cannot possibly exist. This is because every trip departs on top of the hour, and thus any trip has a duration of *at least* 1 hour. Regarding the return value, there is no way of immediately checking whether a speed value is the answer during a single iteration of binary search. If we make the range of the halving to be inclusive (eg. `l = m` instead of `l = m + 1`) to account for this we will end up in an infinite loop. To remedy this problem we can keep the last validated speed in a separate variable `ret`, and return that once the binary search has completed.  

#### Conclusion

This solution has a time complexity of $O(n\log s)$ where $n$ is the length of `dist` and $s$ is the size of the search space. Validating a speed against `dist` takes $O(n)$ time, which we perform $O(\log s)$ times during the binary search against the search space of $s$. The space complexity is $O(1)$.  