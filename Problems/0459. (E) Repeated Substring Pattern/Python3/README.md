## 459. (E) Repeated Substring Pattern

### `solution.py`
An easy solution is to simply examine all possible substrings and check whether they can be contatenated to form the string `s`. We can speed things up by realizing that only prefixes with lengths that `len(s)` can be cleanly divided by potentially be valid. For all such prefix substring `k`s, we create a string `k * (len(s) // len(k))` and compare it against `s`. If the two strings are equal we can immediately return `True`. Otherwise, if all prefixes evaluate to false, it means that `s` cannot be constructed with one of its substring and so we return `False`.  

#### Conclusion
This solution has a time complxity of $O(n\cdot \sqrt{n})$ where $n$ is the length of `s`. Building the concatenated string and comparing it against `s` takes linear time, and (through a bit of mathematical reasoning) there can be at most $\sqrt{n}$ factors for some number $n$. The space complexity is $O(n)$, as we create a string of length $n$ for every possible prefix `k`.  
  

### `solution_2.py`
We can improve upon the first solution by realizing that we can think around these strings in the context of rotations. A rotation of a string involves shifting a string a certain amount, where the portion of the string that runs off the edge wraps around to the opposite side. For example if the string `abcdefg` was rotated 3 characters to the right, it would result in the string `efgabcd`.  
The key premise is this; if a string is a repeat pattern of its substring, then all of its rotations are rotations of themselves. Through this we can reason that a string is a repeated pattern if it is a rotation of itself. We can verify this by realizing that a rotated string `r_s` can be thought of as having two parts about the pivot index `i` (the first character of the original string `s`). The first part `r_s[:i]` which is equal to `s[:-i]`, and the second part `r_s[i:]` which is equal to `s[:i+1]`. If we create a new string `t` by contatentating the original string to itself (`t = s + s`) `r_s` *must* be a substring of `t`. As mentioned earlier, we can think of `r_s` as having two parts `A` and `B`. Naturally 'un-pivoting` `r_s` to yield the original string `s` would result in these two parts swapping positions to `BA`. If we contatenate `s` to itself, we would get `BABA` - at which point it becomes obvious as to why this fact is true.  
We have established that a string is a repeated pattern if it is a rotation of itself. Hence, we want to verify whether `s` is a substring of `t = s + s` to determine whether `s` is indeed a repeating pattern. However we do not know by how much `s` has been rotated and must check for all possible rotations. This can be accounted for by removing the first and last characters of `t`.  

#### Conclusion
The time complexity is $O(n^2)$, since Python's `in` keyword on a string takes quadratic time. This may be reduced to $O(n)$ if a different algorithm such as [KMP](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm) were to be utilized. The space complexity is $O(n)$.  
  

