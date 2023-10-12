## 2251. (H) Number of Flowers in Full Bloom

### `solution.py`
This problem essentially boils down to finding the number of overlapping intervals at a given position. Because `flowers` is not sorted, we would have to iterate over `flowers` to count the intervals for 1 position, which would take too long. We can shorten the time complexity by sorting `flowers` first, which allows us to find the relevant interval using binary search. `flowers` however, is a list comprised of lists of length 2. Which element should we be sorting `flowers` by, and how can we determine the number of overlapping intervals using binary search? The key here is to realize that the number of flowers in bloom given a time `t` is simply the number of flowers that have started blooming before `t` subtracted by the number of flowers that have finished blooming before `t`. Both values can be efficiently determined using binary search, but we will now have to keep 2 lists in memory; one containing the sorted starting times and another storing the sorted ending times.  


#### Conclusion
This solution has a time complexity of $O((m+n)\log n)$ where $m$ is the length of `people` and $n$ is the length of `flowers`. `flowers` is sorted twice, where each sort takes $O(n\log n)$ time. For each value in `person` 2 binary searches are performed on a list of length $n$, thus taking $O(m\log n)$ time to process the entierety of `person`. The space complexity is $O(n)$ because the sorting step uses $O(n)$ memory and 2 lists of length $n$ are kept in memory.  
