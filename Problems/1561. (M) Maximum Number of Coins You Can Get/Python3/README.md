## 1561. (M) Maximum Number of Coins You Can Get

### `solution.py`
Because we can only take the second-largest pile of coins among a selection of 3, we essentially have to 'sacrifice' a pile that is larger than ours every time we pick one. As we want to maximize the number of our coins, the most optimal arrangement is to have Alice take the largest pile in `piles` and us take the second largest, while Bob takes the smallest pile. We repeat this process on the remaining piles in `piles` until there are no piles remaining.  
Sorting `piles` in descending order, we can simulate the steps described earlier by simply taking the sum of the piles that we will be taking. As Bob will take the smallest piles, the latter third of the sorted `piles` can be ignored. Alice will start off by taking the largest value, after which we take the second largest value. Hence we will be taking every other pile in the sorted `piles`, starting at the 2nd pile.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `piles`. Sorting `piles` takes $O(n\log n)$ time, and the summation step that follows takes $O(n)$ time. The space complexity is $O(n)$ due to the sorting step.  
  

