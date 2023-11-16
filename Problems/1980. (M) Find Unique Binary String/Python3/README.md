## 1980. (M) Find Unique Binary String

### `solution.py`
Because `nums` contains `len(nums) == n` *binary* numbers that are also `n` long, it is guaranteed that we can find a binary number of length `n` that is not already in `nums`. As all values in `nums` are unique, we can simply convert all values in `nums` to base 10 integers and find any value that is not in the converted `nums`. We first convert the string literals into integers and store the values in a `set`. Then we simply start looping with a counter of `0`. We check whether the counter is in the set. If yes, we increment the counter by `1` and check it against the set again. If not, we immediately exit the loop and return the binary representation of the integer as a string. As values are allowed to have leading zeros on the left, we pad the string with `"0"`s until the return string has a length of `n`.  

#### Conclusion
This solution has a time complexity of $O(n^2)$, where $n$ is the length of `nums`. We convert `nums` into a set, and hashing a string of length $n$ takes $O(n)$ time. Finding a unique value takes $O(n)$ times as the worst case is when `nums` contains values in the interval $[0, n)$. The space complexity is $O(n)$.  
  


### `solution_2.py`
Another valid approach is to recursively build the string. Starting with an empty string, we will incrementally build it up by adding a `"0"` or a `"1"`. The base case is when the string is `n` long, at which point we see whether the string already exists in `nums` by checking it against a set containing the strings in `nums`. This algorithm as-is has a time complexity of $O(2^n)$ since each recursion recurses on 2 possible choices. Similar to the first solution, we can immediately stop whenever we find a valid string to avoid generating all possible binary strings of length `n`. We simply return a 'dummy' value (in this case, `None`) when it is determined that a string is invalid(already in `nums`). WLOG, we first try recursing by adding a `"0"` to the string. We then try the other option *only when* it is determined that the string constructed by taking the initial option is invalid.  

#### Conclusion
The time and space complexity for this solution is identical to the first. The recursion step takes $O(n^2)$ time (because we recurse on $O(n)$ states and string concatenation in Python takes $O(n)$ time), and the recursion stack uses $O(n)$ memory.  
  


### `solution_3.py`
There is an even better solution that takes a mathematics-based approach. The concept in question is called [Cantor's diagonal argument](https://en.wikipedia.org/wiki/Cantor%27s_diagonal_argument#Uncountable_set). Without going into too much detail, given a set of binary numbers of the same length, we can construct a binary number that does not exist in the set by setting its digits to the opposite of each of the values in the set. For instance, we take the 1st digit of the 1st value, flip it, and use the result as the 1st digit of our value. We do the same for the 2nd digit of the 2nd value, and the 3rd, and so on, until we end up with a number with `n` digits.  
In order to avoid ending up with the same time complexity as the previous solutions, we store each digit in a list `ret` and use `.join()` instead of using string concatenation to construct the string.  

#### Conclusion
The time and space complexity of this solution is $O(n)$. We do not perform any preprocessing on `nums`, but do access 1 digit of each value, which takes $O(n)$ time. We store each digit of the resulting binary value in `ret`, which will use $O(n)$ memory.  
  

