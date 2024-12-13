## 2558. (E) Take Gifts From the Richest Pile

### `solution.py`
Given the list of integers `gifts`, we are asked to determine the remaining number of gifts(sum of `gifts`) after `k` seconds. The following steps are performed each second:  

- Select the pile(element) with the largest number of gifts. If there are multiple such piles, select any one of them.  
- Leave only the floor of the square root of the number of gifts and remove all others.  

We can trivially simulate the problem by using a max heap, stepping through each step until we reach the desired epoch. Once we reach `k` seconds, we simply take the sum of all values remaining in the heap. Note that Python's built in `heapq` module only offers a minimum heap, which we work around by negating all values being inserted in and out of the heap.  

#### Conclusion
This solution has a time complexity of $O(n\log n + k\log n)$, where $n$ is the length of `gifts`. Initializing a heap with the contents of `gifts` finishes in $O(n\log n)$ time. During the simulation step, an element is popped off of the heap each second. Since we step through `k` seconds, this step will take $O(k\log n)$ time to complete. Finally, the summation step removes all items from the heap, and completes in $O(n\log n)$ time. Thus, the overall time complexity of this solution is $O(n\log n + k\log n)$. The space complexity is $O(n)$, due to the heap `heap`.  
  

