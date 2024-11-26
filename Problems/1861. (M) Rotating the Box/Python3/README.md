## 1861. (M) Rotating the Box

### `solution.py`
The 2D list `box` represents the contents of a box viewed from its side. A single 'cell' in a box can either contain a stone(represented by a `#`), a fixed obstacle(represented by a `*`), or be empty(represented by a `.`). When the box is rotated(tipped over) 90 degrees clockwise, the contents of the box are subject to the effects of gravity, making loose objects fall downwards. The contents of the box interact with this gravity in the following manner:  

- Stones will drop vertically downwards until it either encounters another stone, an obstacle, or the bottom of the box.  
- A stone stops moving immediately when it encounters another object.  
- Obstacles stay fixed in place, and does not move.  

This problem can be largely split into 2 parts. Rotating `box` and its contents, and applying the gravity effect to the elements of `box`. Here we will apply the rotation first, after which we will apply the gravity effect.  
Instead of messing with indices, we can simply transpose `box` and then reverse the rows of the transposed list in order to rotate `box` 90 degrees to the right. We can then start applying gravity to `box` in accordance to the behavior described previously. Because the occupied portion of a column can only grow taller as each stone is processed, we can use 2 pointers when processing a single column. One pointer will point to the current cell that needs to be processed, and another will point to the index of the first unoccupied cell from the bottom of the box. Examining cells from the **bottom** of the box, if the current cell contains a stone we swap it out with the bottom-most empty cell. If the current cell contains an obstacle, we update the other pointer to point to the cell above the current one. Once all columns have been processed, we can directly return the updated 2D list.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `box`. Rotating `box`, as well as applying gravity to the rotated list each require $O(mn)$ time to complete. The space complexity is $O(1)$, excluding the returned 2D list `res`.  
  

