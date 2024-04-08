## 1700. (E) Number of Students Unable to Eat Lunch

### `solution.py`
This problem can be easily solved by simply simulating it by using a queue and a stack. In Python, we would instantiate a new `collections.deque` passing `students` in as the argument, and we can simulate a stack by maintaining an index to the 'topmost' element. While the queue is not empty, we attempt to serve each and every student currently in the queue. Popping a student from the queue, we requeue that student if their preference does not match the topmost sandwich. Otherwise, we simulate popping off the served sandwich from its stack by incrementing the pointer by `1`. After each round of attempted servings, we check whether a serving has actually happened or not. If it has, we try another round of serving. Otherwise we return the number of students remaining in the queue.  

#### Conclusion
This solution has a time complexity of $O(n^2)$ where $n$ is the length of `students`. Each round of attempted servings takes $O(n)$ time to perform, and there can be at most $O(n)$ rounds that can be performed(a very loose estimate). The space complexity is $O(n)$, since we instantiate a new `deque` using the contents of `students`.  
  

