## 752. (M) Open the Lock

### `solution.py`
We can easily solve this problem by realizing that it is analoguous to a graph traversal problem. The combination will be a vertex, and the neighbors of a vertex will be combinations that differ from it by only 1 move. Since we want the minimum number of operations that will unlock the lock, we would need to find the shortest path between `0000` and `target`, which means that we should be using BFS to traverse the 'graph' of combinations.  
As setting the lock to any combination in this list will seize the lock, we want to initialize the set of 'visited nodes' with the contents of `deadends`. Then, we initialize a Python deque that only contains `0000` since this combination is the one we are asked to start from. While the deque `nodes` is not empty, we pop an item from the queue and check whether it has been visited or it is equal to `target`. For the former, we simply move on to the next combination in the queue. For the latter, we immediately return the current 'path length' which corresponds to the number of operations that have been made to the lock  up to this point. Otherwise, we try all possible changes to the current combination. If the traversal exits without returning, it means that there is no path from `0000` to `target`, making it impossible to unlock. We return `-1`, as requested by the problem.  

#### Conclusion
This solution has a time complexity of $O(1)$. Or, if $n$ is the length of `deadends`, $O(n)$. The search space is fixed regardless of the input(`0000` to `9999`). Hence, it can be argued that the time complexity is $O(1)$ as the asymptotic behavior of the algorithm does not scale to the size of the input. The other option is to scale the running time to the size of `deadends`, in which case we count the initialization of `visited` as taking $O(n)$ time. The space complexity is $O(n)$, where $n$ is the length of `deadends`.  
  

