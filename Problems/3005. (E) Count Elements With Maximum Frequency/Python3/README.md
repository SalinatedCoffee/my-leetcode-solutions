## 3005. (E) Count Elements With Maximum Frequency

### `solution.py`
We immediately see that we should be using counting sort. Once we have the frequencies of all values in `nums`, we can iterate over them to determine the number of values that appear most frequently, and in turn use that value to return the desired value. There are a number of ways to achieve this, but here we have opted to use Python's built in `Counter` object to count the frequencies of the elements in `nums`.  

#### Conclusion
The time complexity of this solution is $O(n+k)$, where $n$ is the length of `nums` and $k$ is the number of unique values in `nums`. However, because the problem constraints state that the range of $n$ and $k$ are equal, we can rewrite the time complexity as $O(n+k) = O(n+n) = O(n)$. The space complexity is also $O(k) = O(n)$.  
  


### `solution_2.py`
In the previous solution, we had to make 2 passes over the frequency list; once to determine the max frequency, and once again to count the number of elements with that max frequency. We can eliminate this step altogether by counting the number of max frequencies as we iterate over `    nums` instead. Two variables are required; one that keeps track of the largest frequency up to the current point in time, and another that keeps track of the number of unique values in `nums` with that frequency. As we iterate over `nums`, we first update the frequency count for the current element. Then we compare the updated value against the historical maximum, after which there are 2 options. If the newly updated frequency is larger than the historical, we update the historical maximum and reset the element count to `1`. If the updated frequency is equal, we simply increment the element count by `1`. We do nothing otherwise. Once we finish iterating over `nums`, we simply return the product of the maximum frequency and the element count.  

#### Conclusion
The time and space complexity of this solution are identical to the previous solution.  
  

