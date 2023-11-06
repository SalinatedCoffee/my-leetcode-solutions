## 1535. (M) Find the Winner of an Array Game

### `solution.py`
Actually performing the game would be unoptimal, as we would have to shuffle integers around every turn. Since we are only interacting with the first two values in the list, a linked list based data structure *could* be used to reduce overhead. However, this still requires the use of extra memory to store the linked list copy of `arr`.  
We can instead think of two scenarios - either `k` is larger than or equal to `len(arr)`, or it is not. For the former, it is not that difficult to realize that the largest value in `arr` would win. For the latter however, we will need to simulate the game in order to determine the winning value.  
Instead of actually modifying `arr`, we maintain two pointers which each point to the '`0`'th and '`1`'st values in `arr`. Whenever the left value (the '`0`'th value) wins, we simply advance the right value by `1`, simulating the 'push' to the end of the array. When the right value wins, we now make it the left value and advance the right pointer by `1`. In both cases, we need to remember to wrap around the indices by taking the modulo of `len(arr)` to avoid running into index errors.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `arr`. When `k >= len(arr)`, we return `max(arr)`, which is a $O(n)$ operation. Otherwise we simulate the game, which is also a $O(n)$ operation. The space complexity is $O(1)$.  
  

