## 1475. (E) Final Prices With a Special Discount in a Shop

### `solution.py`
The list of integers `prices` represents the price of each item, where `prices[i]` is the price of the `i`-th item. When purchasing an item, the item may be eligible for a discount. The discounted amount is the price of the `j`-th product that satisfies the conditions `i < j` and `prices[j] <= prices[i]`. That is, the current item may be discounted by the price of the *first* product that has a price of less than or equal to the current item. If such a product does not exist, the full price of the item must be paid. Given `prices`, then, our task is to return the list of prices that needs to be paid for each product.  
This problem can be trivially solved through brute force, as the constraint on `prices` is sufficiently small. We can use nested for loops to iterate over `prices`, scanning over the relevant portion of `prices` for each item.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `prices`. The discounted price is evaluated for each and every item in `prices`, which takes $O(n)$ time as the size of the 'relevant' portion of `prices` for each item is bound by $n$. The space complexity is $O(1)$, excluding the returned list `res`.  
  

