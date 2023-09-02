## 338. (E) Counting Bits

### `solution.py`

As mentioned in the follow-up question, an algorithm that runs in $O(n\log n)$ time is trivial to implement and would involve converting all values in the range $[0, n]$ to binary. We can however, do better by reusing previously computed values to determine the value of some number.  
Realizing that we *can* reuse previous values is very straightforward, but working out the *how* and *what* is the difficult part. When counting bits for some integer `i`, we cannot simply refer to `i-1` as there is no well-defined relation for the number of `1`s for cases where the next binary number would add a new digit (for example `0b111` to `0b1000`). Thankfully, we are working with binary numbers and so we know that we can shift a number towards the right by dividing it by 2. If we start counting bits in ascending order (which is how the problem wants the answer to be ordered) it is guaranteed that by the time we are trying to count the bits of some integer `i`, we would have already determined the counts for all values in the range $[0, \texttt{i})$. Among these values, the one we are interested is that of `i // 2`. This value will be the number of `1`s in the binary representation of `i` **shifted 1 towards the right**, and it is trivial to determine whether the LSB of `i` is `1` or not. Now we only need to check the remainder of `i` when divided by `2` and count it if necessary.  
Note that in Python integers have no max value and so we are forced to use `%`, but in other languages such as C or Java where integers do have a fixed size it would be faster to use bit manipulation instead.  

#### Conclusion

The solution has a running time of $O(n)$ where $n$ is `n`. It uses $O(n)$ memory as `ret` will contain $n+1$ elements.  
