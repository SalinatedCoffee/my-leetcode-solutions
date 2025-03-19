## 1352. (M) Product of the Last K Numbers

### `solution.py`
We are asked to implement the `ProductOfNumbers` class and its 2 methods `.add` and `.getProduct`. A `ProductOfNumbers` accepts a stream of integers through the `.add` method, and returns the product of the `k` last added integers by calling `.getProduct(k)`.  
The brute force approach would be to simply store all integers added by `.add` and computing the appropriate product on the fly every time `.getProduct` is called. Looking at the problem constraints however(`.add` and `.getProduct` will be called at most `4 * 10^4` times), we can see that this approach would be too slow for it to be feasible. Going back to the problem description, we can see that `ProductOfNumbers` does not support the removal of values that have already been added. We also notice that we are only returning the products of the added integers, which means that if any of the integers being multiplied is `0`, the product will also be `0`. As `.getProduct(k)` should return the product of the `k` recently added values, we can 'forget' all currently added values whenever a `0` is added.  
A `ProductOfNumbers` instance will have a list `_prods`, which will contain all of the precomputed products for the integers added after the last added `0`. Initially, `_prods` will only contain a single value of `1`. When `.add` is called, we first check whether the value to be added is `0`. If so, we reset `_prods` to its initial state(`[1]`) since any call to `.getProduct` that would include the currently added value would result in a value of `0`. Otherwise, we simply precompute the cumulative product by appending the product of the last value in `_prods` and the added number to `_prods`.  
When `.getProduct(k)` is called, we first check whether if there are enough elements in `_prods` to answer the question. In `.add`, we reset `_prods` whenever we are given a value of `0`. If `k` is larger than the length of `_prods` - `1`, we know that the last `k` added items contains a `0`, which means the product will always be `0`. Otherwise, we calculate the value appropriately and return it.  

#### Conclusion
Instantiating a `ProductOfNumbers` object finishes in $O(1)$ time, and will use $O(n)$ space over the lifetime of the object, where $n$ is the number of calls made to `.add`.  
A single call to `.add` will finish in $O(1)$ time, using $O(1)$ extra memory.  
Calls to `.getProduct` also completes in $O(1)$ time, using $O(1)$ extra memory.  
  

