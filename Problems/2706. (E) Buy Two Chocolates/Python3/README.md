## 2706. (E) Buy Two Chocolates

### `solution.py`
We want to buy 2 chocolates from `prices` with a budget of `money`, where the objective is to minimize the total cost. The problem also asks us to make the purchase in a way that leaves us with a non-negative amount of money, but we can ignore this step for now as minimizing the cost of the chocolates also optimizes for this part of the problem.  
As with simple problems such as this, there are many valid approaches that can be taken. But because they all boil down to one idea we will take the most optimal approach of them all. To minimize the cost of the pair of chocolates, we essentially want to buy the 2 cheapest ones. Thus, the task at hand now becomes that of finding the 2 smallest elements in `prices`. This can be easily achieved by iterating over the list while keeping track of 2 integers; the smallest value, and the second smallest value observed up to the current item. If the current item is smaller than the smallest value, the previously smallest value now becomes the second smallest and the current value becomes the new smallest value. If it is not, it still may be smaller than the second smallest value and so we update it if necessary. Finally, we check whether the chocolates are purchasable with the given budget and return the appropriate value.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `prices`. We iterate over `prices` once, and for each element we only perform a handful of operations that each take constant time to complete. The space complexity is $O(1)$.  
  

