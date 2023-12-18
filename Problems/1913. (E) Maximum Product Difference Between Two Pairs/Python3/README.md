## 1913. (E) Maximum Product Difference Between Two Pairs

### `solution.py`
In order to maximize the product difference we must choose 2 pairs of integers that would each produce the largest and smallest products. Because all elements in `nums` are positive, we can simply select the two largest / smallest values. If we sort `nums` access to these values becomes trivial as they would be the first and last 2 values.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$ where $n$ is the length of `nums`. `nums` is sorted using Python's built in sort, which takes $O(n\log n)$ time to complete. The space complexity is $O(n)$, also due to the sorting step.  
  


### `solution_2.py`
We can also find the relevant values by iterating over `nums` instead of sorting it. While iterating along `nums`, we keep track of 4 integers containing the two largest / smallest values seen up to the current value in `nums`. WLOG, if the current value is larger than the largest seen we update the largest and second largest. If not, we update the second largest accordingly. As `nums` is guaranteed to contain at least 4 elements, the 4 integers are also guaranteed to be unique. We can now simply compute the product difference and return it.  

#### Conclusion
This solution has a time complexity of $O(n)$. `nums` is iterated over once, and for each value in it we perform a fixed number of constant time operations. The space complexity is $O(1)$.  
  

