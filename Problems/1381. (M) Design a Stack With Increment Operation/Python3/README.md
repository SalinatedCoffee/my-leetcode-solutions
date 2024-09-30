## 1381. (M) Design a Stack With Increment Operation

### `solution.py`
We are asked to implement the class `CustomStack` which behaves just like a typical stack but also supports an increment operation on the *bottom* `k` items. In addition to a constructor that accepts a max capacity as an integer, `CustomStack` should implement the following methods:  

* `push(x)`, where `x` is an integer: If the stack is not full, pushes `x` onto the stack.  
* `pop()`: Removes the top-most item off of the stack and returns it. If the stack is empty, this method should return `-1`.  
* `inc(k, val)`, where `k` and `val` are integers: Increments the *bottom* `k` elements by `val`. If the stack contains less than `k` elements, this method will effectively increment all elements by `val`.  

Because the size of the stack is fixed, we can easily implement `CustomStack` by using a list to internally store the elements and an integer to mark the top of the stack. Using a list to store elements has the added benefit of being able to access the items through an index, which will make implementing the increment functionality easier.  
`CustomStack` will have two instance variables. The list of integers `_items`, and integer `_top`. When a `CustomStack` object is instantiated, `_items` will be initialized as a list of length `k` and filled with `-1`. `_top` will be initialized as `0`, and will represent the index of the item after the top-most item in the stack. When `pop()` is called, we temporarily store the element at `_top - 1` before decrementing `_top` by `1`. The stored value is then returned. When `increment(k, val)` is called, we simply iterate over the first `k` elements of `_items`(or up to the index of the last valid element, whichever is smaller) while incrementing each value by `val`.  

#### Conclusion
Instantiating a `CustomStack` object requires $O(k)$ time to complete, where $k$ is the capacity of the `CustomStack`, which is `k`. Calls to `pop` and `push` take $O(1)$ time to finish, whereas a call to `increment` will take $O(k)$ time to complete. A `CustomStack` object will use $O(k)$ memory during its lifecycle.  
  

