## 799. (M) Champagne Tower

### `solution.py`
We can simulate this problem by determining the amount of champagne that flows through a cup given the amount that is poured. For example, if we pour 10 units of champagne to the cup in the first row, 9 units will overflow to the 2 cups in the next row, with half overflowing on each side. If we 'left-justify' the pyramid so that it now resembles a right triangle, we can say that the overflow from the `0`th cup in row `0` flows into the `0`th cup in row `1` and the `1`st cup in row `1`. Using this relationship we can now run a simulation on a pyramid with `query_rows` rows of glasses, and return the contents of the desired glass when the simulation is finished.  

#### Conclusion
The time and space complexity of this solution is $O(n^2)$, where $n$ is `query_rows`.  
  

