## 881. (M) Boats to Save People

### `solution.py`
Before we try anything, let's first work out exactly *how* we can determine the minimum number of required boats. We cannot simply put any valid pair in a boat, as there may be some other person that makes use of the available `limit` more efficiently. For example, let `person = [1, 2, 2, 6]` and `limit = 7`. We can put `1` and `2` in the same ship as the total weight will be under the limit. After that `2` and `6` will have to take separate ships since their total weight will be over the limit. However, if we had paired `1` with `6` instead of `2` the remaining people could have taken the same ship, reducing the number of ships from 3 to 2.  
Based on this idea, we can sort `people` in ascending order and maintain two pointers that each point to the remaining lightest and heaviest person respectively. If the pair of people denoted by the pointers are over the limit, we simply put the heavier person on their own boat as that is the optimal choice. Else we simply put both in the same boat.  
One detail to keep in mind is to continue until the left pointer is *strictly larger* than the right pointer, since we want to cover the case where there is only one person remaining.  

#### Conclusion
This solution takes $O(n\log n + n)$ time to run, where $n$ is the length of `people`. Sorting `people` takes $O(n\log n)$ time, after which it is traversed exactly once. The space complexity is $O(1)$ as the sorting is performed in-place (though technically Python and Java's implementation of Timsort uses $O(n)$ memory).  
  
