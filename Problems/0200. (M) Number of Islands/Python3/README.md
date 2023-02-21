## 200. (M) Number of Islands

### `solution.py`
We need to count the number of *contiguous* stretches of land, and thus need to figure out a method to efficiently group squares in a set-like structure. Python `set`s will most likely not work as when given a square there is no way to retrieve the set of which that square is an element of. Disjoint-sets would be a good fit in this case since we can efficiently check whether two elements are in the same set or not, and also merge two sets in optimal time.  
The parent nodes of each square is stored in the 2D list `p`, where the default value is the node itself. We then traverse all squares within `grid` via BFS, merging the current square with the previous one if both of them are land squares.  
Once the traversal has completed we count the number of disjoint sets by iterating through all squares in `grid` one more time.  

#### Conclusion
The solution uses $O(mn)$ time and space, where $m$ and $n$ are the dimensions of `grid`.  
  

### `solution_2.py`
Instead of explicitly maintaining multiple sets we can simply 'color over' the land squares using some form of [flood fill](https://en.wikipedia.org/wiki/Flood_fill) whenever we encounter a land square, and count the number of initial calls to flood fill. Modifying the input is generally considered bad practice however, and so we will create a deep copy of `grid` and modify it instead.  

#### Conclusion
This solution also uses $O(mn)$ time and space, but runs faster than the first solution since the overhead from using a disjoint-set to group land squares is eliminated.  
  

