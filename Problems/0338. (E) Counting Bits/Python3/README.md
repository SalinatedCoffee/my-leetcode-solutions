## 338. (E) Counting Bits

### `solution.py`
As mentioned in the follow-up question, an algorithm that runs in $O(n\log n)$ time is trivial to implement and would involve converting all values in the range $[1, n]$ to binary. We can do better however as we can obviously reuse previously computed values to determine the value of some number.  
Realizing that we *can* reuse previous values is very straightforward, but working out the *how* and *what* is the difficult part. We can't simply refer to `i-1` as there is no simple relation for cases where a new digit would be added (for example `0b111` and `0b1000`). Thankfully we are working with binary numbers so we know that we can shift a number towards the right by dividing it by 2, and we would have already determined the count for the value `i // 2`. Now we only need to count the first digit which we can trivially do by dividing the number by 2 and looking at the remainder.  
Note that in Python integers have no max value and so we are forced to use `%`, but in other languages such as C or Java where integers have a fixed size it would be faster to use bit manipulation instead.  
  
#### Conclusion
The solution has a running time of $O(n)$ where $n$ is `n`. It uses $O(n)$ memory as `ret` will contain $n+1$ elements.  
  

