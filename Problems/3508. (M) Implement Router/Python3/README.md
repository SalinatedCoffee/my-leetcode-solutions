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

Upon reading the requirements, we can see that there are multiple layers to the problem. The FIFO nature of adding and forwarding packets can be solved by using a deque. Counting the number of packets with timestamps within a specific interval can be done using binary search. Grouping packets by their destination can be achieved through a dictionary. Storing the packets in a set will allow us to quickly determine whether a packet already exists in storage.  
The problem now becomes determining how we would put all of these components together when implementing the `Router` class.

#### Conclusion
\<Content\>  
  

