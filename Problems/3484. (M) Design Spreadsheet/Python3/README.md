## 3484. (M) Design Spreadsheet

### `solution.py`
We are asked to implement the class `Spreadsheet`, which represents a spreadsheet and supports a small set of operations against its cells. The spreadsheet should support the following:  
- 26 columns labeled from `A` to `Z`
- Any number of rows, specified during object instantiation
- An empty cell initially contains a value of `0`
- A cell can hold a single integer within the range $[0, 10e5]$
- Ability to set the value of a cell (`Spreadsheet.setCell`)
- Ability to reset the value of a cell to `0` (`Spreadsheet.resetCell`)
- Ability to compute the value of `A + B` where `A` and `B` can be either a non-negative integer or cell reference in the form of `CN`(where `C` is the column label and `N` the row number) (`Spreadsheet.formula`)

First off, we can see that we can sparsely store the cell values by using dictionaries instead of a 2D list. If we first use a dictionary to map column labels to their corresponding `defaultdict`s, we will naturally get a `0` upon indexing an empty cell, which allows us to avoid having to manually check the existence of the requested cell.  
When a `Spreadsheet` object is instantiated, we also instantiate a dictionary called `_sheet`. The dictionary is initialized with 26 key-value pairs, using the column labels as the keys and empty `defaultdict(int)`s as the values. Note that `rows` is not used here, since storing the values sparsely allows our `Spreadsheet` object to store any number of rows.  
The methods `Spreadsheet.setCell` and `Spreadsheet.resetCell` are trivial to implement: for the former, we simply parse the cell reference and assign the given value to the appropriate cell. For the latter, we can save on memory by deleting the cell if it exists.  
`Spreadsheet.getValue` is slightly more involved as we have to parse the formula string. Thankfully, we are only asked to support addition with 2 values, which makes the parsing step trivial to implement.  


#### Conclusion
Instantiating a new `Spreadsheet` object completes in $O(1)$ time. Calls to all methods (`Spreadsheet.setCell`, `Spreadsheet.resetCell`, and `Spreadsheet.formula`) also finish in $O(1)$ time. Finally, a `Spreadsheet` object has a space complexity of $O(m)$, where $m$ is the maximum number of unique cells with a non-zero value over the object's lifetime.  
  

