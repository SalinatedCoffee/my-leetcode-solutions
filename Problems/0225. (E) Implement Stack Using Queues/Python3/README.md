## 225. (E) Implement Stack Using Queues

### `solution.py`
A stack is a last-in-first-out (LIFO) data structure, where at a certain point in time only gives access to the item that was most recently added. Queues on the other hand, are a FIFO data structure and gives access to the earliest added item. The obvious problem that arises from this difference is that we do not have constant time access to the last added item by using queues. We do however, know exactly where this element is in the queue, and can reach it by almost emptying the queue until its last element. And while emptying the queue, if we store the items in another queue in the order that they are removed we will essentially have a copy of the original queue without the most recent added item.  
Thus when `MyStack` is instantiated we also instantiate 2 deques; (Python does not have a built-in vanilla queue[^1]) queue `_a` which will be the 'primary' queue and queue `_b` which will be the secondary. We also initialize an integer `_last` to cache the most recently added item. When `push()` is called we simply add the item to the primary queue and update `_last`. When `pop()` is called we empty the primary queue into the secondary queue excluding the last item, while updating `_last`. We then swap the two queues so that the primary queue is now secondary, then pop and return the last remaining item in `_b`. This is of course a linear-time operation, but we can do this since we know that `MyStack` can contain at most 99 items, which is a relatively small number. For `peek()`, we can save time by simply returning `_last` instead of emptying the primary queue as we did for `pop()`. Finally we trivially implement `empty()` by checking whether the primary queue is empty or not.  

[^1]: *Technically* it does, but it's a niche module where its primary intended usage is in multithreaded code - and even then, `collections.deque` is more performant and also thread-safe so you should probably be using `deque` anyway.  

#### Conclusion
The time complexity of `__init__`, `push()`, `peek()`, and `empty()` is $O(1)$. `pop()` has a time complexity of $O(n)$, where $n$ is the number of items that `MyStack` currently contains. The space complexity is also $O(n)$.  
  

### `solution_2.py`
We can also implement a solution that uses a single queue by realizing that we can 'empty' the queue into itself. If the queue contains `n` items, we can pop an item and immediately re-add it to the queue `n-1` times to expose the most recently added item. Using this technique, we only need to modify `pop()` for the solution to be accepted.  

#### Conclusion
Identical time and space complexity to the first solution.  
  

