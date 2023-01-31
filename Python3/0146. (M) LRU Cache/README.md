## 146. (M) LRU Cache

### `solution.py`
This is a classic design problem, and one of the easier ones to implement. When adding an item to a full [LRU Cache](https://en.wikipedia.org/wiki/Cache_replacement_policies#Least_recently_used_(LRU)) it simply evicts the item that has not been accessed for the longest time (hence, Least Recently Used) to make space for the new item. There are multiple ways of implementing this behavior, but we can use Python's `collections.dict` since it 'remembers' the insert order of items since Python 3.7+ (at the time of writing, LeetCode uses Python 3.10).  
The solution simply removes an item and adds it back to `self._items` whenever it is accessed. When the cache is at capacity and a new item is added it removes the left-most item in `self._items` and adds the new one.  

#### Conclusion
Because items are stored in a dictionary, `get()` and `put()` runs in $O(1)$ average time as requested by the problem. `LRUCache` overall uses $O(n)$ space where $n$ equals `capacity`, for obvious reasons.  
Another valid solution would be to use `OrderedDict` instead of `collections.dict`, which supports reordering operations like `move_to_end()`. Both have their pros and cons, but generally `collections.dict` performs marginally better in terms of element access.  
  
  