## 2678. (E) Number of Senior Citizens

### `solution.py`
The list `details` contains strings of length 15 that each represents a single passenger. A string is comprised of multiple sections, but the substring we are interested is the substring of length 2 starting at the 12th character. This substring is comprised of digits and represents the passenger's age, and we are asked to count the number of passengers that are strictly more than 60 years old.  
In order to determine a passenger's age, we can simply extract the 2 character substring through slicing and convert it into an integer. Because we want to count the number of elements in `details` where this value is strictly larger than 60, we can use `filter(f, details)` to only leave the element `details[i]` where `f(details[i])` returns `True`, for all `i` in the range `[0, len(details))`. The expression `int(details[i][11:13])` extracts the integer age of the string `details[i]`, and combining this with the `filter()` invocation we get the expression `filter(lambda x: int(x[11:13]) > 60, details)`. This call returns an iterator that yields the strings of all passengers in `details` that are more than 60 years old, and to count these strings we need to evaluate the iterator into a list and return its length. As such, the solution can be written as the single line `return len(list(filter(lambda x: int(x[11:13]) > 60, details)))`.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `details`. `filter` examines every element of `details`, using $O(1)$ time to evaluate whether an element should be included or not. Thus, the overall time complexity of this solution is $O(n)$. The space complexity is also $O(n)$, due to the intermediate casting of the generator returned by `filter` into a list.  
  

