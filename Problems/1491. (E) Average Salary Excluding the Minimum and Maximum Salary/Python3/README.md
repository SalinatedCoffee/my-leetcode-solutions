## 1491. (E) Average Salary Excluding the Minimum and Maximum Salary

### `solution.py`
We cannot know whether a number is either the smallest or largest in its array until we have examined every other number. Hence we would need to iterate over the entirety of `salary` in order to determine the minimum and maximum salaries. Once the iteration is complete we simply need to subtract the min/max salaries from the total and divide it by the length of `salary` subtracted by 2.  

#### Conclusion
This solution has a running time of $O(n)$ where $n$ is the length of `salary`, since `salary` is iterated over once. The space complexity is $O(1)$.  
  

### `solution_2.py`
Another approach is to simply sort `salary`, which makes removing the min/max values trivial.  

#### Conclusion
The time complexity of this solution is $O(n\log n)$ since Python's (and Java's) built-in sort uses Timsort which takes $O(n\log n)$ time.  The space complexity is $O(n)$, which is also due to the use of Timsort.  
  
