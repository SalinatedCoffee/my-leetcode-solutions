## 1431. (E) Kids With the Greatest Number of Candies

### `solution.py`
This is an easy problem, so a simple linear solution should suffice here (even without the difficulty label, sometimes the simplest solution is indeed the best solution). We can simply find the greatest number of candies in `candies` first, and build a list by iterating through `candies` again and making comparisons using the maximum number of candies we found in the previous step.  

#### Conclusion
This solution has a time and space complexity of $O(n)$ where $n$ is the length of `candies`. We iterate over `candies` twice, and `ret` will have a size of $n$.  
  

