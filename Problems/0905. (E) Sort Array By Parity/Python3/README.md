## 905. (E) Sort Array By Parity

### `solution.py`
As is usually the case for simple problems like this, there could be multiple ways that this problem can be solved. Here however, we will take the easiest approach that populates 2 arrays. While iterating through `nums`, we take the modulo 2 of a value to determine whether it is odd or even. We then append it to the appropriate list. Once all values have been categorized we extend the even list with the odd list, after which we can simply return the combined list.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. The space complexity is also $O(n)$  
