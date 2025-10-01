## 3508. (M) Implement Router

### `solution.py`
We are asked to design and implement the `Router` class, which will emulate a networking router. It should support the following methods and functions:  
- Each packet consists of 3 values; `source`, the unique ID of the machine that generated the packet, `destination`, the unique ID of the target machine, and `timestamp`, the time at which the packet arrived at the router.
- `memoryLimit` is the maximum number of packets that the router can keep in memory, and is provided upon object instantiation.
- The method `Router.addPacket()`, which takes the integers `source`, `destination`, and `timestamp`, and returns a boolean.
  - If the packet already exists in the `Router` object, ignore it and return `False`.
  - If the `Router` object contains `memoryLimit` packets, remove the *oldest* packet, add the new one, and return `True`.
  - Otherwise, add the packet and return `True`.
- The method `Router.forwardPacket()`, which takes no arguments and returns a list of integers.
  - Remove the oldest packet from storage, and return it in the form `[source, destination, timestamp]`.
  - If the storage is empty, return an empty list.
- The method `Router.getCount()`, which takes the integers `destination`, `startTime`, and `endTime`, and returns an integer.
  - Return the number of packets in storage with destination `destination` and timestamp in the range `[startTime, endTime]`.
- Assume that the timestamp is non-decreasing across all calls to `Router.addPacket()`.

Upon reading the requirements, we can see that there are multiple layers to the problem. The FIFO nature of adding and forwarding packets can be implemented by using a deque. Counting the number of packets with timestamps within a specific interval can be done using binary search. Grouping packets by their destination can be achieved through a dictionary. Storing the packets in a set will allow us to quickly determine whether a packet already exists in storage.  
The problem now becomes determining how we would put all of these components together when implementing the `Router` class. We keep track of the stored packets in 3 different 'components'. A deque to determine which packet should be forwarded next, a dictionary that maps a destination address to the list of packets that have that address as their destination, and a set to keep track of which packets are currently stored in the `Router` instance.  
When `.addPacket()` is called, we first check whether if the given packet is already stored or not. If so, we immediately return `False`. Otherwise, we move on to the next step, checking whether if the current `Router` instance is at capacity. If so, we evict the oldest packet from memory by calling `.forwardPacket()`. We can now add the packet to storage by updating the set of stored packets, pushing the new packet into the deque, and appending it to the appropriate list based on its destination address.  
For `.forwardPacket()` we simply pop a packet off of the deque and remove it from its destination packet list and set of stored packets. We then convert the tuple to a list before returning it.  
Finally `.getCount()` should look up the list of packets corresponding to the given destination, and count the number of packets that are timestamped within the time interval. Since all packets are stored in the order they arrive, we can speed things up by performing binary search and computing the number of packets instead of linearly scanning through the list.  

#### Conclusion
Initializing a `Router` instance finishes in $O(1)$ time. Calls to `Router.addPacket()` also take $O(1)$ time to run, and uses $O(1)$ extra memory. Calls to `Router.forwardPacket` runs in $O(n)$ time, since removing the forwarded packet from its destination packet list is a $O(n)$ time operation. Finally, calls to `Router.getCount()` has a running time of $O(n\log n)$ as it uses binary search to determine the number of packets.  
A `Router` object has a space complexity of $O(n)$, where $n$ is the number of packets stored.  
  

