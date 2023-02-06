## 1470. (E) Shuffle the Array

### `solution.py`, `solution_oneline.py`
A simple solution is to create a list of length `2*n`, and iterate over `nums` copying the elements to the appropriate location.  
The one-liner solution uses the same basic concept, but utilizes list comprehensions instead of explicit `for` loops. In nested list comprehensions, the inner comprehension is evaluated first.  
  
#### Conclusion
The solution uses $O(n)$ time and space.  
  

### `solution_2.py`
An in-place solution does exist... but coming up with an algorithm that only uses swaps to move elements around is [not as simple as one may think](https://arxiv.org/abs/0805.1598). So here we'll take a more specific approach where we use bitwise operations to store two numbers in a single element. Look at the constraints on the numbers in `nums`, the maximum value a number can have is $10^3 = 1000$, which is 10 bits long in binary (`1111101000`). This means that we can store any number in `nums` as long as we have space to store 10 bits. Now we can store two numbers in a single element by bit shifting a number 10 bits to the left and bitwise-ORing it with another number.  
The in-place algorithm first uses the aforementioned steps to 'collapse' the upper half of `nums` onto the first half, and then expands the lower half to the correct positions. One thing to note is that we must expand in reverse order starting from the last element in the lower half, to avoid overwriting numbers.  
  
#### Conclusion
This solution uses $O(n)$ time, but uses $O(1)$ space.  
I'm personally a bit conflicted on answers like this - it's very easy to break and feels like a hack that doesn't generalize that well to different situations... but to each their own, I guess.  