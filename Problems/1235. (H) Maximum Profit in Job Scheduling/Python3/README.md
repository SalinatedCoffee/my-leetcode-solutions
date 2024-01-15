## 1235. (H) Maximum Profit in Job Scheduling

### `solution.py`
When we finish a job, we need to find the next available job which is the one with the smallest value of `startTime` that is larger than the `endTime` of the current job. Searching for this job would take us linear time, as the given arrays are not sorted. If we sort the three arrays based on the values in `startTime`, we can easily find the next job that satisfies the conditions. We can then see that the problem now becomes a dynamic programming one, as we can incrementally build up towards the desired answer.  
If `jobs` is an array sorted by `startTime`, where `jobs[i]` is the triple `(startTime[j], endTime[k], profit[l])`, we can determine the profit of scheduling `jobs[i:]` if we know the corresponding value for `jobs[i+1:]`. Of course, we can only schedule `jobs[i+1]` if it does not overlap `jobs[i]`. Instead, we find the first schedulable job through binary search as `jobs` is sorted in order of `startTime`. Once we have done so there are two choices that can be made; we can either schedule the current job and move on to the next schedulable one, or simply skip the current job and move on to the next job in `jobs`. Either way, we want to select the choice that yields the most amount of profit, which is then returned.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `startTime`(and consequently, the other 2 lists). The initial sorting step and the dynamic programming step both take $O(n\log n)$ time. The values for all $n$ states are computed, with each computation taking $O(\log n)$ time to perform due to the use of binary search. The time complexity is $O(n)$ as the sorting step and memoization of the recursive states each use $O(n)$ memory.  
  

