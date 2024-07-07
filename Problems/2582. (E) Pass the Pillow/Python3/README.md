## 2582. (E) Pass the Pillow

### `solution.py`
Given the integers `n` and `time`, we are asked to return the index of the person holding the pillow after `time` seconds. There are `n` people standing in a line, and initially the first person holds the pillow. Every second, the pillow is passed to the next person in the line. When there is no next person to pass the pillow to, it is passed in the opposite direction. For example, let `n = 3`. Initially, the `0`th person will be holding the pillow. After 1 second, the `1`st person will be in possession of the pillow, and the `2`nd person the second after that. After another second passes, there is nobody else that the `2`nd person can pass the pillow to, and thus he/she passes it to the `1`st person. This problem can obviously be solved by using simply division and modulo operations. The one thing to keep in mind is that it takes `n-1` seconds to pass the pillow down the entire line, not `n`. When we evaluate `time % (n-1)` then, we will get the index of the person holding the pillow after `time`, but we also need to know the direction in which the pillow was travelling in order to determine the correct value. This can be easily determined by looking at the quotient of `time // (n-1)`. If it is even, the pillow was travelling in the original direction. Otherwise, it was travelling in the opposite direction. In either situation, `time % (n-1)` returns a value in the range `[0, n-2]`, which means it excludes the very last person in whichever direction. Thus, the index of the person while the pillow was moving in the original direction is simply `time % (n-1) + 1`, and in the opposite, `n - time % (n-1)`.  

#### Conclusion
This solution has a time and space complexity of $O(1)$.  
  

