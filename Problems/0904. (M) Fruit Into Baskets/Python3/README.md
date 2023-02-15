## 904. (M) Fruit Into Baskets

### `solution.py`
Reading through the problem description, we realize that the problem boils down to finding the longest interval containing at most 2 distinct elements. To do this we can use two pointers while maintaining the element types and number of those elements within the interval bounded by the two pointers. In the trivial case where the rightmost element (`fruits[j]`) is already being counted or it is not with room for another 'basket', we simply update the dictionary `baskets`, check the number of picked fruits against the current maximum, and move on. On the other hand if it is not being counted and there is no room for another basket we simply start incrementing the left pointer (`i`) decrementing the count until we can make room for another basket.  

#### Conclusion
The solution at most iterates over `fruits` twice, and `baskets` does not scale with the size of the input. Thus it takes $O(n)$ time to run and uses $O(1)$ space.  
  

### `solution_2.py`
Thinking about the non-trivial case where `fruits[j]` does not have a basket and there are 2 baskets already, we can skip incrementing `i` if we know the location of the rightmost instance of `fruits[i]`, and the number of instances of `fruits[j]` between that location and `i`. Instead of iterating from `i` to `j` we can set `i` to the rightmost instance location, evict the basket for `fruits[i]`, and subtract the encountered number of instances of `fruits[j]` from the current number of `fruits[j]`. After this operation, `fruits[i:j+1]` will only be comprised of `fruits[j]`. Here we realize that instead of the previously mentioned algorithm we can simply keep track of the current streak of the same fruit, that is, the length of the streak and the type of fruit comprising the streak. This way whenever the next fruit breaks the current streak (it is either a new fruit entirely or it is the fruit just before the current streak), we can simply update the length of the current streak and the type of fruit instead of incrementing `i`. As an added bonus this eliminates the need for two indicies and a dictionary, since we only need to know what the current position is and the 'baskets' are implicitly tracked in a queue-like manner.  

#### Conclusion
This solution has the same time and space complexity as the first one, but should run much faster in practice thanks to the removal of the pointer `i` and the use of two integers instead of a dictionary.  
  

