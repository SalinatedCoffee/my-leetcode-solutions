## 719. (H) Find K-th Smallest Pair Distance

### `TLE.py`
Given the list of integers `nums`, we are asked to return the distance of the pair of integers in `nums` where its distance is the `k`th smallest among all pairs in `nums`. The distance of a pair is simply the absolute difference between the two values. The obvious brute force method would be to generate the distances of all possible pairs, then sorting them to determine the `k`th smallest distance. While not as intuitive, we can also use binary search to find this distance. Given some distance `d`, if we can count the number of pairs in `nums` that have a distance less than or equal to `d`, we know that distances less than `d` will never yield more pairs than `d`. This allows us to perform binary search on the pair distance, using the intial search space `[0, max(nums) - min(nums)]`. Naturally, the most intuitive way of counting the number of valid pairs is to simply iterate over all possible pairs in `nums`. We can now implement our binary search algorithm, selecting the right half if there are less than `k` pairs for the midpoint distance and the left half otherwise.  

#### Conclusion
This algorithm has a time complexity of $O(n^2\log m)$ where $n$ is the length of `nums` and $m$ is the largest pair distance in `nums`. For $n$ number integers there are $n(n+1)/2)$ possible ways of selecting a pair of values. Since all pairs are considered for every evaluation of a midpoint during the searching step, and the initial search space is of size $O(m)$, the overall time complexity comes out to be $O(n^2\log m)$.  
  

### `solution.py`
The previous attempt unfortunately takes too long to run and will fail with TLE. The most obvious piece of code that we can improve is the counting step, which   

#### Conclusion
\<Content\>  
  

