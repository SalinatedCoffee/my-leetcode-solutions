## 1282. (M) Group the People Given the Group Size They Belong To

### `solution.py`
Since we are guaranteed that there is at least one valid answer, we may disregard edge cases such as `groupSizes = [1, 1, 4]` where some people belong in a group that ends up with fewer people that its supposed size. Then the problem becomes trivial, in that we may greedily match people into their respective groups and start a new group whenever a group becomes full.  
We maintain a 2D list `groups`, where `groups[i]` is the group of people that belong to a group of size `i`. While iterating over `groupSizes`, we first check if the `i`th person's group is full. If it is, we add that group to the return list `ret` and start a new group. We then add the `i`th person to `groups[groupSizes[i]` and move on to the next person. Once everyone has been put into a group, we do a last pass on `groups` and add any non-empty group to `ret`, after which we can return immediately.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `groupSizes`. `groups` has a length of $n$, thus initializing it will take $O(n)$ time. `groupSizes` is iterated over once, and each iteration takes constant time to process. Hence, the overall time complexity is $O(n)$. The space complexity is also $O(n)$, since `groups` can at most contain $n$ integers.  
