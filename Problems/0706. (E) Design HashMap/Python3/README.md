## 706. (E) Design HashMap

### `solution.py`
Since we already know the range of potential keys, we can simply allocate a single list and store values using their keys as the index to that list. But for fun and profit, (and in the spirit of preparing for an interview) we will take a slightly more 'hashmap-like' approach. As the input range is $10^6$, we will 'split' this domain in half, using the first 3~4 digits to designate a bucket, and the remainder to handle collisions.  
When `MyHashMap` is instantiated, we allocate a list of `None`s of length 1001. We use a length of 1001 instead of 1000 to trivially hash key `1000000` without using any additional condition checks. Given a `key`, we 'split' it into half according to the method described previously. We first divide by `1000` to get the bucket, then take the modulo `1000` to avoid any collisions. If either the bucket or the actual value is `None`, it means that the key does not exist in the hashmap and so we return `-1`.  

#### Conclusion
Instantiation of `MyHashMap` has a time complexity of $O(k)$, where $k$ is the size of the input range of possible keys. `MyHashMap.put()` also takes $O(k)$ time to run, since it will instantiate a list of size $O(k)$ whenever a bucket does not exist. `MyHashMap.get()` and `MyHashMap.remove()` both take $O(1)$ time to run, which is in line with most implementations of a hashmap. The overall space complexity is $O(k)$, since in the worst case where every bucket is populated `self._bucket` will contain 1001 lists of length 1000.  
Note that a more proper implementation will also include a dynamic scaling feature based on a specified load factor, where the hashmap will grow and shrink in size based on the number of key-value pairs it contains. Here however, since the values are all integers, we can take a brute-force approach like this since `MyHashMap` will end up using a reasonable amount of memory even in the worst case (approximately 4 megabytes with 4 byte integers).  
  

