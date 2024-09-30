## 432. (H) All O'one Data Structure

### `solution.py`
We are asked to implement the class `AllOne`, which is a data structure that keeps track of the frequency of each inserted string. `AllOne` should implement the following methods:  

* `inc(key)`, where `key` is a string: If `key` exists, increment its value by `1`. Otherwise, add it to the `AllOne` instance and set its value to `1`.  
* `dec(key)`, where `key` is a string: Decrement `key`'s value by `1`. If the value is already `1`, remove `key` from the `AllOne` instance. `key` is guaranteed to exist in `AllOne` when `dec(key)` is called.  
* `getMaxKey()`: Return any key with the largest value in the `AllOne` instance.  
* `getMinKey()`: Return any key with the smallest value in the `AllOne` instance.  

All of the described methods should run in $\Theta(1)$ time.  
The $\Theta(1)$ running time restriction on the methods is what makes this problem difficult; we cannot sort the values or use a naturally ordered data structure like a heap. We need to devise a more creative solution, which we can do at the cost of using more memory. Notice that we can only in/decrement a string's frequency by `1`. This means that if we think about these frequencies laid out on a number line, we only need access to the two neighboring values of a key's frequency. If we represent the ordered list of frequencies as a doubly linked list, we can assign a new frequency to a key in constant time if we have constant time access to the 'frequency node' corresponding to that key. For example, assume that we have an `AllOne` object containing the strings `"abc"`, `"xyz"`, and `"ijk"`, each having the frequency `1`, `5`, and `11`. The internal linked list would look like `1 <-> 5 <-> 11`, with each node containing a set of strings that have the frequency of itself. In this example, Node `1` would have a set that contains `"abc"`. We also introduce a dictionary that maps a string to its frequency node. When a string's frequency is modified, we retrieve the string's frequency node and 'move' the string to either one of its neighbors. To ensure that the linked list only contains relevant frequency nodes, we remove a frequency node from the list if it's set of strings is empty. This way we can guarantee that the head and tail node in the linked list is always valid, eliminating the need to iterate over the list in search of a valid node(which would violate the $\Theta(1)$ restriction).  
  

#### Conclusion
Initializing an `AllOne` object takes $O(1)$ time to complete, and uses $O(1)$ additional memory.  
Calls to the methods in the problem description, as well as the helper method `_insert_new`, all take $O(1)$ time to complete as they modify a fixed number of nodes in the internal linked list and the keys are all stored as either a key to a dictionary or in a set. A single call to these methods require $O(1)$ extra memory, but an `AllOne` object will use $O(n)$ space over its lifetime, where $n$ is the number of calls made to `inc` and `dec`.  
  

