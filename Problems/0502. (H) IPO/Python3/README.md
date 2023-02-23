## 502. (H) IPO

### `solution.py`
The difficulty of this problem comes from realizing that you need to use multiple data structures to solve it, and figuring out what and how to integrate said data structures.  
First off we can keep things simple and consider what the best course of action would be if we can only complete a single project. In this case it would obviously be working on the project with the highest profit yield. So we need to find a project that we can afford to work on which also has the highest profit. Manually scanning `profits` and `capital` every time would be too inefficient - we can just `zip` the two lists together and sort by `capital`. Now we have a list of tuples in ascending order of the first element.  
Better, but still not good enough - we still have to iterate over the sorted list to find the most profitable project, and we have to remember which projects we have already completed. Since our budget strictly increases and projects are sorted according to capital, we *could* store all available projects and update the store as needed. Is there a data structure that supports fast inserts and removals while ensuring that its elements are sorted...? Yes there is, and they're called priority queues(or heap queues, whichever tickles your fancy). For some odd reason Python `heapq`s only implement min-heaps, where elements are sorted in ascending order. We want the opposite behavior so that we can retrieve the largest element in optimal time. Since we're working with integers, we can work around this limitation by negating the element being inserted.  
Now we can keep track of the location of the first unavailable project in the sorted list, and insert the profits of all available projects in the heap. We then pop a project off of the heap, add the profit to our current budget, and repeat these steps `k` times. We can stop early whenever our heap is empty as that would indicate that there are no more projects that we can work on.  
  
#### Conclusion
This solution runs in $O(n\log n)$ time where $n$ is the number of projects, as the sorting step takes $O(n\log n)$ time and element insertion/removal from a priority queue each takes $O(\log n)$ time.  
The space complexity is $O(n)$, as the sorted list and priority queue uses $O(n)$ memory.  
  
