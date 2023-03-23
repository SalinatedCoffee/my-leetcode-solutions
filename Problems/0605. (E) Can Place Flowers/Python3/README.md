## 605. (E) Can Place Flowers

### `solution.py`
The first course of action is to attempt a brute force solution where we manually try and plant as many flowers as possible. We simply check the left and right plots (except for when the current plot is either the first or last one) and plant a flower if they are both empty.  
We may exit early whenever we plant `n` flowers.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the size of the flowerbed. The space complexity is $O(1)$.  
  

