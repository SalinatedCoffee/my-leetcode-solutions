## 2462. (M) Total Cost to Hire K Workers

### `solution.py`
At each round, we must hire the candidate with the lowest cost from two pools of candidates. The two pools are simply `candidates` candidates from either ends of `costs`. If we maintain these pools as two min heaps, we can optimally choose the candidate with the lowest cost for each step. Since the index of a candidate does not matter (unless a tiebreaker is required) we can simply store the first and last `candidate` number of costs from `costs` into `pool_l` and `pool_r`, respectively. Keeping track of the next candidate to be inserted in each pool (`l` and `h`), we can compare the top of both heaps and add to the total the smaller of the two costs. If they are the same, we select the candidate from `pool_l` since the problem asks us to use the index of a candidate as a tiebreaker. When replenishing candidate pools, we must first check whether `l <= h` to avoid considering a candidate that is already in a pool. If a pool cannot be replenished we simply skip the replenish step altogether.  

#### Conclusion
The time complexity of this solution is $O((k+m)\log m)$, where $k$ is `k`, and $m$ is `candidates`. Initializing the two pools takes $O(m\log m)$ time, since they are of size $O(m)$ and converted into a min heap. The hiring step iterates $k$ times, and at each iteration we perform a fixed number of operations on a heap of length $O(m)$ - resulting in an overall running time of $O(k\log m)$. The space complexity is $O(m)$, since both pools have a size of $O(m)$.  
  

