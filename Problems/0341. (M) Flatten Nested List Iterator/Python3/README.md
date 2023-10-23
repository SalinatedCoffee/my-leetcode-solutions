## 341. (M) Flatten Nested List Iterator

### `solution.py`
As we are implementing an *Iterator*, there are a few pitfalls we should be avoiding in our designin. One, we should try to amortize the flattening as evenly as possible. Simply flattening the list during initialization is trivial to implement. However, as the number of elements increase a front-loaded approach like this becomes less viable, especially in a practical setting. Two, we should aim to be using as little memory as possible. Iterators are most often used to lazily access a sequence of values, where it can be argued that the whole point of lazy loading is to conserve resources as much as possible. Again if we were to flatten the list during initialization, we would have to keep all elements in memory, where in reality the user calling your iterator might only access the first `10` elements.  
Our immediate instint is to use recursion to flatten lists as they are encountered. Recursive functions however cannot be 'paused' to return an intermediate answer, which is the opposite of what we want. Instead, we can use a stack to store any upcoming elements. When `NestedIterator` is initialized, we reverse the provided `nestedList` and use that as our stack. Popping off the top of the stack will allow us to access the elements in `nestedList` in the correct order. When `next()` is called, we simply return the integer value of the `NestedInteger` object on top of the stack. Finally when `hasNext` is called, we first peek the top of the stack. If the correspongind `NestedInteger` is indeed an integer, we simply return `True`. If not, we flatten the list by pushing its content on top of the stack. We then peek the top of the stack again, and continue flattening if needed. We return `False` when the stack is empty.  


#### Conclusion
The constructor of `NestedIterator` has a time and space complexity of $O(n)$, where $n$ is the number of elements in `nestedList`. Calls to `next` takes $O(1)$ time and uses $O(1)$ memory, as we simply pop an item off the top of the stack `self._h`. `hasNext` has a time and space complexity of $O(n)$.  
  

