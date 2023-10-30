## 1356. (E) Sort Integers by The Number of 1 Bits

### `solution.py`
For this problem, we are essentially sorting a list of integers using 2 keys. The primary key is the number of raised bits, while the secondary key is simply the value of the integer. Thankfully, integers in Python 3.10 onwards support the `.bit_count()` method which returns the number of raised bits in the binary representation of the integer. This combined with the fact that Python's `sort()` is a [stable sort](https://en.wikipedia.org/wiki/Sorting_algorithm#Stability) allows us to simply sort `arr` 2 times to achieve the effect we want. We first sort `arr` in ascending order by the value of the integers. Then we sort `arr` again using the number of raised bits.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$ where $n$ is the length of `arr`. `arr` is sorted 2 times using Python's built-in sort. Each sort takes $O(n\log n)$ time, and `int.bit_count()` used in the second sorting pass takes $O(1)$ time. The space complexity is $O(n)$ since the built-in sort uses $O(n)$ memory.  
  

