## 2807. (M) Insert Greatest Common Divisors in Linked List

### `solution.py`
Given `head`, the head node of a singly linked list, we are asked to modify the list by 'interleaving' it with new nodes. A new node should be created and linked between each adjacent pair of nodes in the original list, containing the greatest common divisor of its two neighboring nodes. If there is only 1 node in the list, we should return the list as-is.  
Inserting a new node between two adjacent nodes is trivial, as well as computing the GCD of two integers when using Python's built in `math` module. Due to this, we will implement our own GCD function(which is also rather simplistic) in the spirit of learning. We maintain two aptly named pointers `prev` and `cur` as we traverse the linked list, with `cur` pointing to the 'current' node, and `prev` to the one behind it. For each pair of `prev` and `cur`, we take their values and compute the GCD using the [Euclidean algorithm](https://en.wikipedia.org/wiki/Euclidean_algorithm). A new node is then instantiated and linked between `prev` and `cur`, after which both pointers are updated to point to `cur` and `cur.next` respectively before repeating the described steps. When `cur` points to `None`, there are no more adjacent node pairs remaining in the linked list and we return `head`.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the number of nodes in the linked list having `head` as its head node. The linked list is iterated over exactly once, and the instantiation and linking of a GCD node takes $O(1)$ time to complete. The worst case time complexity of the Euclidean algorithm is known to be $O(h)$, where $h$ is the number of digits of the smaller value. Since a value of a node can be at most `1000`, we may consider this operation to be constant. The space complexity is $O(1)$.  
  

