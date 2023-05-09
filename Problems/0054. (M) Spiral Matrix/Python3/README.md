## 54. (M) Spiral Matrix

### `solution.py`
The behavior we want is easy to understand; actually implementing it in code is the difficult part. If we traverse an edge in a single 'step' things can get complicated fast, as we would need to keep track of the direction we need to move towards (left to right? top to bottom? reversed?) and the ranges. Instead we can greatly simplify things by traversing all four sides in a single 'step', and updating the boundaries after. We keep track of four indices that represent the vertical and horizontal ranges of the current step. During each step we iterate across the elements in the appropriate order and 'shrink' the boundaries by increment/decrementing the four indices mentioned earlier. The loop exits when either pair of indices meet each other, at which point we need to check whether there are any remaining elements that have not been added to the return list yet. There are only two possible scenarios; either a column needs to be added moving from top to bottom, or a row moving from left to right. If the matrix is taller than it is wide we should go for the former, and otherwise the latter. Either way, we can trivially add the remaining elements using a single for loop.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `matrix`. The space complexity is also $O(mn)$, if `ret` is taken into account.  
  

