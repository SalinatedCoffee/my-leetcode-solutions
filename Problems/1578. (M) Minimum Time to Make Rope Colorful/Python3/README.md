## 1578. (M) Minimum Time to Make Rope Colorful

### `MLE.py`
We can easily devise a dynamic programming approach for this problem. If we know the minimum time it takes to make `colors[i:]` colorful, we can use that information to compute the minimum time it takes to make `colors[i-1:]` colorful. In order to determine whether the `i`th balloon must be removed or not, we need to know the color of the previous balloon. Each state in our recurrence relation will be represented by two variables `i` and `last`, where `i` is the current balloon being considered and `last` the color of the previous balloon. If `colors[i] != last`, there are two choices we can make. We can either skip the `i`th balloon or remove it. Because we do not yet know what the color of the next balloon is, we need to consider the option of removing the current balloon. For example, say we have three balloons `grr` and are currently considering the second balloon. If we only had the option of removing the current balloon we would end up removing all of the balloons colored `r`, when it would have sufficed to only remove one. In order to compute the minimum cost at the current balloon `i`, we need the minimum cost of making `colors[i+1]` colorful. The return value of recursing on `i+1` is exactly this value, which we can return directly if we choose not to remove the current balloon. If we do choose to remove the `i`th balloon, we add `neededTime[i]` to the returned value and return it. If `colors[i] == colors[last]` we have no choice but to remove the current balloon, and so we compute and return the appropriate value. When `i` is larger than or equal to `len(colors)` we have considered all of the balloons given to us, so we return `0`.  

#### Conclusion
This algorithm has a time complexity of $O(kn) = O(26n) = O(n)$ where $n$ is the length of `colors` and $k$ is the number of unique colors in `colors`. Because each recursive state is represented by two values, with one bound by $n$ and the other by $k$, there are $O(kn)$ states total. We compute the return value of all possible states, and processing each state takes constant time. Therefore, the overall time complexity is $O(kn)$. The space complexity is also $O(kn)$, since we memoize the value of each state.  
  


### `solution.py`
Unfortunately, the previous attempt fails with MLE. This tells us that we should reduce the total number of states, which would reduce the memory used for memoization. If we think about the algorithm in the first approach, we realize that we can simply 'split' `colors` in intervals of homogenous colors. For example, if we had `colors = "ggrrrrr"` we would process the substrings `"gg"` and `"rrrrr"` instead of recursing on individual balloons. By doing so we can eliminate `last` from our recurrence relation, since it is now guaranteed that the previous balloon will always have a different color than the current one. Returning to the example, if we were considering the 3rd balloon we would look ahead to determine the window of identical balloons, which in this case would end at the 7th balloon. We remove all balloons except for the one that would take the longest time to do so, and recurse on the 7+1 = 8th balloon.  

#### Conclusion
The time and space complexity of this solution is $O(n)$.  
  


### `solution_2.py`
We can take the previous solution one step further and get away with not using dynamic programming at all. It was briefly mentioned that we should be removing all balloons in a homogenous interval *except* for the one that would take the most time to remove. Since this strategy is deterministic, we do not need to use dynamic programming. Instead, we iterate over `colors` while greedily leaving the balloons with the longest removal time in its interval. We take the sum of the time it would take to remove the others, and return that value.  

#### Conclusion
This solution has a time complexity of $O(n)$. `colors` is iterated over once, and each balloon takes constant time to process. The space complexity is $O(1)$, as we no longer memoize intermediate states.  
  

