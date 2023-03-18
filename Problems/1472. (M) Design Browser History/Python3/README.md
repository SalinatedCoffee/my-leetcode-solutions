## 1472. (M) Design Browser History

### `solution.py`
At first glance, intuition tells us that this can easily be implemented using a doubly linked list. This is trivial to implement, and we just have to make sure that there are no dangling references left after `visit()` runs.  

#### Conclusion
The time and space complexities are shown below:  
|  | Time | Space |
| --- | --- | --- |
| `BrowserHistory` | * | $O(n)$ |
| `.visit()` | $O(n)$ | $O(1)$ |
| `.back()` | $O(n)$ | $O(1)$ |
| `.forward()` | $O(n)$ | $O(1)$ |
  
A list-based implementation (or vectors for other languages) would also be viable here, as we only add new nodes to one side of the list. The implementation would have the same space complexity while reducing the time complexity of the operations to $O(1)$, as we can access all elements by index in constant time.  
  
