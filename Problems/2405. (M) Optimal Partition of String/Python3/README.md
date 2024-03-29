## 2405. (M) Optimal Partition of String

### `solution.py`
We want the *minimum* number of partitions, so we should try a greedy solution. A greedy algorithm in this context would involve making a partition as big as possible. Iterating over `s` from left to right, we simply 'consume' as many letters as possible before creating a new partition. Thankfully implementing such a solution is rather simple; we maintain a set of letters in the current partition while iterating over `s`. If a character is not in the set we add it and move on. If it is in the set we empty the set, increment the partition counter `ret`, and add the letter to the set before moving to the next character.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `s`. The space complexity is $O(1)$, since there will be 26 items in the set `cur` at most.  
  

