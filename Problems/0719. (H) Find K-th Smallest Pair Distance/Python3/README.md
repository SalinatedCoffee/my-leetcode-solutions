## 719. (H) Find K-th Smallest Pair Distance

### `TLE.py`
Given the list of integers `nums`, we are asked to return the distance of the pair of integers in `nums` where its distance is the `k`th smallest among all pairs in `nums`. The distance of a pair is simply the absolute difference between the two values. The obvious brute force method would be to generate the distances of all possible pairs, then sorting them to determine the `k`th smallest distance. While not as intuitive, we can also use binary search to find this distance. Given some distance `d`, if we can count the number of pairs in `nums` that have a distance less than or equal to `d`, we know that distances less than `d` will never yield more pairs than `d`. This allows us to perform binary search on the pair distance, using the intial search space `[0, max(nums) - min(nums)]`. Naturally, the most intuitive way of counting the number of valid pairs is to simply iterate over all possible pairs in `nums`. We can now implement our binary search algorithm, selecting the right half if there are less than `k` pairs for the midpoint distance and the left half otherwise.  

#### Conclusion
<<<<<<< HEAD
This algorithm has a time complexity of $O(n^2\log m)$ where $n$ is the length of `nums` and $m$ is the largest pair distance in `nums`. For $n$ number integers there are $n(n+1)/2$ possible ways of selecting a pair of values. Since all pairs are considered for every evaluation of a midpoint during the searching step, and the initial search space is of size $O(m)$, the overall time complexity comes out to be $O(n^2\log m)$.  
  

### `solution.py`
The previous attempt unfortunately takes too long to run and will fail with TLE. The most obvious piece of code that we can improve is the counting step, which previously took $O(n^2)$ time to complete. This was because we took a brute force approach in counting the number of viable pairs. Can we devise a method that counts the pairs more efficiently?  
Given some distance `d`, we want to determine the number of pairs of elements in `nums` that have a distance less than or equal to `d`. If we want to do so without having to iterate over all elements of `nums`, we need some sort of information relating to the given problem. In this case, this would be the value of `d` and some element `nums[i]`. Given these values, we know that we can form valid pairs between `nums[i]`, and any value in `nums` that have a value in the range `(nums[i], nums[i]+d]`. That is, we need a way to quickly determine the number of values in `nums` that are less than or equal to some value. If `nums` is sorted in ascending order, we can precompute these values by performing a single pass over `nums`. Because we want the number of values with regard to the distance, we should be able to retrieve a count for all possible distances. The smallest possible distance is `0`, and the largest possible distance is the largest value in `nums` multiplied by 2(this is because of the initial search space for the binary search step). These values will be stored in the list `pre`, where `pre[i]` will be the number of elements in `nums` that are less than or equal to `i`. `nums` does not contain only unique values however, which means that there may be multiple instances of the value `nums[i]` in nums. When computing the number of pairs between `nums[i]` and values that are not equal to `nums[i]`, this will not be a problem. However, we also need to count pairs that have a distance of `0`, which requires us to know the number of occurrences of `nums[i]` in `nums`. These values will be stored in the dictionary `val`, where `val[i]` is the number of occurrences of `i` in `nums`.  
When `count(d)` is called, we start iterating over the elements of `nums`. For each value, we count the number of pairs between the current element and elements with strictly larger values by looking at the values of `pre`. The number of pairs between occurrences of the current element is computed next by using the values of `val`. After adding the total number of pairs for the current element to the sum, we skip over all other occurrences of the current value and move on to the next element of `nums`. The binary search step is mostly identical to the previous solution, with the initial search space being the same as well.  
  

#### Conclusion
The time complexity of this solution is $O(n\log n + n\log m)$. `nums` is sorted to make populating `pre` easier, and takes $O(n\log n)$ to complete. Binary search is then performed on the initial search space `[0, max(nums) - min(nums)]`, where $\log m$ halvings will occur until the left and right boundaries converge. During each halving `count` is called to determine which half to discard. As described above, `count` iterates over all elements of `nums`, taking $O(1)$ time to process each value. Thus a call to `count` will take $O(n)$ time to complete, bringing the time complexity of the binary search step to $O(n\log m)$. The space complexity is $O(n+m)$. `pre` uses $O(m)$ memory since it scales to the maximum possible distance given `nums`, and `val` takes up $O(n)$ space. Sorting `nums` also requires $O(n)$ memory.  
=======
This algorithm has a time complexity of $O(n^2\log m)$ where $n$ is the length of `nums` and $m$ is the largest pair distance in `nums`. For $n$ number integers there are $n(n+1)/2)$ possible ways of selecting a pair of values. Since all pairs are considered for every evaluation of a midpoint during the searching step, and the initial search space is of size $O(m)$, the overall time complexity comes out to be $O(n^2\log m)$.  
  

### `solution.py`
The previous attempt unfortunately takes too long to run and will fail with TLE. The most obvious piece of code that we can improve is the counting step, which   

#### Conclusion
\<Content\>  
>>>>>>> ff355f6827bf34979fb03d39d933af4241d1657b
  

