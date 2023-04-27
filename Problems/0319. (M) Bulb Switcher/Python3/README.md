## 319. (M) Bulb Switcher

### `solution.py`
This is a rather unusual type of problem that puts emphasis on mathematical reasoning skills rather than knowledge of data structures and algorithms. The gist is recognizing the pattern of the number of bulbs being toggled every round, where an odd number of bulbs are toggled only during perfect square rounds(1st, 4th, 9th... etc). LeetCode's own write up of the [solution](https://leetcode.com/problems/bulb-switcher/editorial/) explains this rather nicely.  

#### Conclusion
The time and space complexity of this solution is $O(1)$. Built-in square root functions typically use the [fast inverse square root](https://en.wikipedia.org/wiki/Fast_inverse_square_root) method, which can compute the square root of relatively smaller numbers in constant time.  
  

