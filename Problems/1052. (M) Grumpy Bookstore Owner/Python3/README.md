## 1052. (M) Grumpy Bookstore Owner

### `solution.py`
Given the lists `customers`, `grumpy`, and the integer `minutes`, we are asked to return the largest number of satisfied customers. `customers` contains the number of customers that are present during each minute, with the value of `customers[i]` being the number of customers present during the `i`th minute. `grumpy` denotes whether the owner is grumpy or not during each minute, with `grumpy[i]` being `1` meaning that the owner is grumpy during the `i`th minute, and `0` otherwise. A customer is satisfied when the owner is **not** grumpy when they are present in the store. We can prevent the owner from feeling grumpy for `minutes` consecutive minutes, which can only be used once. We immediately see that we could take a sliding window approach to this problem, as we can prevent the owner from being grumpy for a consecutive period of time. If we can calculate the number of 'could-have-been' satisfied customers in each window, we can determine the largest value among said windows and in turn compute the largest number of satisfied customers when the 'un-grumpify' window is used.  
We first compute the number of potentially satisfiable customers within the intial window. The rest of `customers` is then iterated over, adding and removing each element of `customers` by looking at the value of `grumpy`. If `grumpy[i]` is `0`, we simply ignore `customers[i]` as they would have been satisfied regardless of the un-grumpify window. Once the iteration completes, we will have the number of the most potentially satisfiable customers, which we can use to compute the desired value.  

#### Conclusion
This solution has a time complexity of $O(n)$, where $n$ is the length of `customers`. Initializing the window takes $O(n)$ time as `minutes` is bound by `len(customers)`. The iteration that follows also takes $O(n)$ time, as well as the final summing step. Hence, the overall time complexity is $O(n)$. The space complexity is $O(1)$.  
  
