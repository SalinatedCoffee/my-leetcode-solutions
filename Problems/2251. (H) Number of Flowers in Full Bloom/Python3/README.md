## 2251. (H) Number of Flowers in Full Bloom

### `solution.py`
This problem essentially boils down to finding the number of overlapping intervals at a given position. Because `flowers` is not sorted, we would have to iterate over `flowers` to count the intervals for 1 position, which would take too long. We can shorten the time complexity by sorting `flowers` first, which allows us to find the relevant interval using binary search. `flowers` however is a list comprised of lists of length 2. Which element should we be sorting `flowers` by, and how can we determine the number of overlapping intervals using binary search?  


#### Conclusion

\<Content\>  
