## 2418. (E) Sort the People

### `solution.py`
Given the list of strings `names` and list of integers `heights`, we are asked to sort `names` in descending order of each element's value in `heights` and return the sorted list. This can be trivially achieved by first generating a list of indices, sorting the list by using `heights` as the sorting criteria, and finally using the sorted list of indices to sort `names` in the correct order. In Python, this can be implemented in a single line by using list comprehensions as we have done here.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `names`(the number of people to be sorted). Because `heights` also has a length of $n$, sorting it using Python's built in sort will require $O(n\log n)$ time to complete. Generating the list of indices, as well as mapping the sorted list of indices to the elements of `names` each takes $O(n)$ time to process, bringing the overall time complexity to $O(n\log n)$. The space complexity is $O(n)$, due to the sorting step and the list of indices which is briefly kept in memory.  
  

