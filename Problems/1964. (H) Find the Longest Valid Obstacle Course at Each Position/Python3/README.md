## 1964. (H) Find the Longest Valid Obstacle Course at Each Position

### `solution.py`
Since a valid course consists of obstacles where they cannot be smaller than the immediately preceding obstacle, this boils down to the classic longest increasing subsequence problem. Like the original problem, we can maintain a list where we store elements that would make up the LIS and build it up by iterating along `obstacles`. The problem is that we cannot possibly keep track of all possible longest subsequences(namely subsequences of identical length), but one subsequence may be more optimal than another. For example, let `obstacles = [1, 6, 2, 3, 4]`. Considering the last obstacle of height `4`, we can see that there are two LISes in `obstacles[:3]` - `[1, 6]` and `[1, 2]`. However, when we extend the range to `obstacles[:4]` `[1, 6]` cannot be extended while `[1, 2]` can be extended to `[1, 2, 3]`. If we make sure that the last obstacle in the stored LIS representation is the shortest one among all subsequences with the same length, the LIS representation is guaranteed to be 'optimal'. Thus at some obstacle `i`, we need to find the index of the first element that is shorter than `i` and overwrite the element if it exists, or extend the list containing the LIS representation. We could do this by linearly scanning the list, but we can use binary search to achieve the same result more efficiently.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$, where $n$ is the length of `obstacles`. We iterate over all elements of `obstacles`, and we perform a binary search on `lis` (which can at most contain $n$ elements) which takes $O(\log n)$ time for each iteration. The space complexity is $O(n)$.  
  

