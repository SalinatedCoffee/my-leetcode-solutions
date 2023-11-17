## 1877. (M) Minimize Maximum Pair Sum in Array

### `solution.py`
With enough experience with DSA problems under your belt, you may immediately recognize this as a greedy algorithm problem. As is typically the case with greedy algorithms however, the difficulty comes not from the implementation, but from proving that such an approach would actually be optimal.  
The gist is that we should be pairing the smallest values with the largest values first as we want to minimize the maximum pair sum of `nums`. In order to prove that this strategy is indeed optimal, let us first assume that we have a list of integers $a_1, a_2, ... a_{n-1}, a_n$ such that $a_1 \le a_2 \land a_2 \le a_3 \land ... \land a_{n-1} \le a_n$. From this list we will select 2 random elements $a_i$ and $a_j$, such that $a_1 \le a_i \le a_n$ and $a_1 \le a_j \le a_n$. Through proof by contradiction, the maximum of the pairs $(a_1, a_i)$ and $(a_j, a_n)$ should **not** be optimal than $(a_1, a_n)$ and $(a_i, a_j)$. Looking at the pairs $(a_1, a_i)$ and $(a_j, a_n)$, it is quite obvious that the sum of $(a_j, a_n)$ will *always* be greater than or equal to that of $(a_1, a_i)$. We see that this inequality also holds true between $(a_j, a_n)$ and the pairs $(a_1, a_n), (a_i, a_j)$. In other words, the pairing of $(a_1, a_i)$ and $(a_j, a_n)$ is indeed *suboptimal* than choosing $(a_1, a_n)$ and $(a_i, a_j)$ - proving that our strategy is optimal by contradiction.  
As mentioned previously, the implementation is simple. We sort `nums` in ascending order and iterate along the first half while computing the sum of pairs moving towards the center. Once the iteration completes we return the largest sum seen.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `nums`. The sorting step takes $O(n\log n)$ after which the sorted list is iterated over once. The space complexity is $O(n)$, also due to the sorting step.  
  

