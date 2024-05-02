## 514. (H) Freedom Trail

### `solution.py`
One might be tempted to take a greedy approach, but upon further ideation it becomes clear that it would not work on this problem as a character can appear multiple times in `ring`. Choosing the element that would require the least amount of steps may not necessarily be the best choice as it might put us further away from the character to be matched after it.  
Instead, we can take a dynamic programming based approach in which we use 2 arguments to keep track of each state; the index of the current character to be matched in `key`(`idx`), and the index of the character in `ring` that is currently in the 12:00 position(`north`). If `idx == len(key)` there are no characters left to match, so we return `0`. Otherwise we try turning the ring to each occurrence of `key[idx]`, taking the smallest path to reach each of them. The number of steps required when turning the ring to each index(`n_pos`) of `key[idx]` in `ring` is the sum of 3 values; the minimum distance required to turn the ring to `n_pos`, the single step required to input a letter with the ring, and the minimum steps required to match the next key character `key[idx+1]` when `ring[n_pos]` is at the 12:00 position.  
By definition of the recurrence relation, we start recursing using `0` for both parameters, as we want to match the entirety of `key`(`key[0:]`) and the first character of `ring` is initially in the 12:00 position.  

#### Conclusion
This solution has a time complexity of $O(m^2n)$ where $m$ is the length of `ring` and $n$ is the length of `key`. Since each state is represented by 2 arguments where they are bound by $m$ and $n$, there are $mn$ states in total, with all of them being evaluated. Processing a single state takes $O(m)$ time as we scan through the indices of each occurrence of a character in `ring`. Hence, the overall time complexity is $O(mn\cdot m) = O(m^2n)$. The space complexity is $O(mn)$, as we memoize the values of each state in memory.  
  

