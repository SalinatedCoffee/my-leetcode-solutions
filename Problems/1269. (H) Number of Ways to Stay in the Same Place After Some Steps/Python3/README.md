## 1269. (H) Number of Ways to Stay in the Same Place After Some Steps

### `solution.py`
Given the length of the array and number of steps, we want to determine the number of possible ways to stay on the `0`th position in the array. For each step there are 3 moves that can be taken; we can either move 1 step towards the left, 1 step towards the right, or simply stay at the current position. If we are currently at some position `p` with `s` possible steps remaining, and we wanted to determine the possible number of ways to return to position `0`, we can see that we would simply need to return the sum of the results of `s-1` steps at positions `p-1`, `p`, and `p+1`. The base cases of this recurrence relation would be when `p` is out of bounds of the array(`p < 0` or `p >= arrLen`), in which case we return `0`. The case where `s == 0` is also a base case, in which case we return `0` or `1` depending on the value of `p`. We only return `1` when `p == 0`, signifying that we have reached position `0` having exhausted every available step given to us.  

#### Conclusion
The time complexity is $O(n\cdot\text{min}(n,m))$, where $n$ is `steps` and $m$ is `arrLen`. The states in the recurrence relation is represented by 2 parameters. `p` represents the current position and `s` represents the remaining number of steps. While `arrLen` determines the domain size of `p`, it is also bound by `steps` since we can only move by `1` during each step. Hence there will be a total of $n\cdot\text{min}(n,m)$ states to evaluate, and with each state taking constant time to compute the overall time complexity becomes $O(n\cdot\text{min}(n,m))$. The space complexity is also $O(n\cdot\text{min}(n,m))$, as we keep the results of each state in memory. The recursion stack can only be $\text{min}(n,m)$ deep, which is outscaled by the memoized results.  
  
