## 950. (M) Reveal Cards In Increasing Order

### `solution.py`
This problem can be solved by simulating the drawing of cards with a queue. As we want to find the ordering of cards that would reveal them in increasing order of their values, we need to sort `deck` in ascending order before beginning the simulation. We also initialize the Python deque `queue_idx` which initially contains the integers from `0` to `len(deck) - 1` in ascending order. The returned list will be `ret`, which is intialized with `0`s before iterating over `deck`. While iterating over `deck`, then, we simulate drawing the cards by popping an element from the queue. The popped item will be where the current card of `deck` will be stored in `ret`; that is, it is the position of the current card in the 'reveal-in-increasing-order' ordering. We then proceed to pop and requeue the next item in the queue(implemented using `deque.rotate()`) before moving onto the next card in the sorted deck. These steps are repeated until every card in `deck` has been processed, at which point `ret` will contain the cards of the given deck in the desired order.  


#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `deck`. Sorting `deck` takes $O(n\log n)$ time, and simulating the drawing of the cards takes $O(n)$ time as we only interact with a queue. The space complexity is $O(n)$, due to the sorting step as well as the queue `queue_idx` where the indices of the cards are intially stored.  
  

