## 6. (M) Zigzag Conversion

### `solution.py`
As I see it there are two ways in solving this problem; we can either lay the original string out in the described zigzag pattern and traverse it, or identify the numeric pattern of indicies that would appear and apply it over the given string. Here, we will take the former approach by 'simulating' the zigzag traversal.  
We initialize a list of strings with length `numRows`, where we will explicitly store the concatenated rows of the zigzag pattern. Then we simulate the actual traversal by setting the row advance direction, flipping between going down and up whenever we encounter the first or last row in the zigzag layout.  
Once the traversal has finished, we may simply concatenate the stored strings in ascending order to achieve the desired result.  

#### Conclusion
The time and space complexity of this solution is $O(n)$, where $n$ is the length of `s`. The traversal step takes $O(n)$ time, and `rows` uses $O(n)$ space.  
  

