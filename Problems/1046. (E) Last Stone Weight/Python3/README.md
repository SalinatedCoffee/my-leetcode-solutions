## 1046. (E) Last Stone Weight

### `solution.py`
For each turn we want fast access to the 2 heaviest stones. We can access these stones in constant time if we store the weights in a max heap. Python heap queues only support min heaps and so we need to apply a 'hack' where we negate value before pushing them into the heap, and negating them again after popping them out of the heap. We keep taking turns while the heap contains more than one stone. During each turn we pop two stones from the heap. If both stones weigh the same, we simply do nothing and move onto the next turn. If not, we push a new stone with weight `y-x` into the heap.  
Once we exit the loop, we either return `0` if the heap is empty, or the weight of the singular stone remaining in the heap.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the number of stones in `stones`. `heappush()` takes logarithmic time based on the size of the heap, which is performed for every stone in `stones`. The space complexity is $O(n)$, as the heap will at most store $n$ items.  
  

