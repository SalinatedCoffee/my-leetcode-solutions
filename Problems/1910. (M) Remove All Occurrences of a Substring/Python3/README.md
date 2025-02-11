## 1910. (M) Remove All Occurrences of a Substring

### `solution.py`
Given the strings `s` and `part`, we can remove the leftmost substring of `s` that matches `part` any number of times. Our task is to return the resulting string after performing as many deletions as possible.  
As the constraints on the size of `s` and `part` are relatively small, we can take a brute force approach to this problem. This involves iterating over `s` to find the leftmost match of `part`, removing that substring from `s`, and repeating the process until `s` no longer contains an instance of `part`. This can be easily achieved by using Python's built in functions; in this case, the `.find()` method can be used to find the index of the earliest occurrence of `part` in `s`. We use the `in` keyword to first determine whether `s` contains `part`. If so, we find the index of the first character of the substring in `s` equal to `part` and remove it from `s` by slicing it out.  

#### Conclusion
This solution has a time complexity of $O(n^2/m)$, where $n$ is the length of `s` and $m$ the length of `part`. The worst case scenario for the while loop is when `s` is simply `part` concatenated multiple times. In this case, the loop will repeat $n/m$ times as we remove the matching substring from `s` for each iteration. A single iteration involves searching `s` for a substring equal to `part`, which requires $O(n)$ time to complete. Hence, the overall time complexity comes out to be $O(n\cdot n/m) = O(n^2/m)$. The space complexity is $O(n)$, due to the use of slicing when removing substrings from `s`.  
  


### `solution_2.py`
We can take a different approach by recognizing that we could use a stack to store remaining characters, which will allow us to avoid constructing a string for every removed substring. Whenever the size of the stack is equal to or larger than `part`, we know that the stack could contain an instance of `part`. If so, we can pop off `len(part)` characters from the stack and compare them against `part` to determine whether the substring actually matches against `part`. If there is a match, we simply move on to the next character in `s`. Otherwise, we revert the stack to its previous state by pushing the popped characters back onto the stack. Once all characters of `s` have been examined, we simply concatenate the contents of the stack back into a string and return it.  

#### Conclusion
The time complexity of this solution is $O(mn)$. A match against `part` is performed whenever a character is pushed onto the stack, and a single match takes $O(m)$ time to complete. Since each and every character of `s` are examined, the overall time complexity comes out to be $O(mn)$. The space complexity is $O(m+n)$ due to `stack`($O(n)$) and `temp`($O(m)$) in the helper function `match_stack()`.  
  


### `solution_3.py`
Because we are searching for occurrences of a string in another string, we can implement a more efficient solution by utilizing the [KMP algorithm](https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm). In a nutshell, KMP preprocesses the pattern being searched for by computing the length of the longest prefix-suffix(LPS) at each index. This information is then used when matching the pattern against a string, skipping ahead in the pattern when a mismatch is detected instead of matching against the pattern from scratch. We use KMP to match `part` against `s` while pushing each character of `s` onto the stack. Whenever a match is detected, `len(part)` characters are popped off of the stack, essentially deleting the substring from `s`. The pointer for `part` is then reset back to `0` before continuing the search.  

#### Conclusion
This solution has a time complexity of $O(m+n)$. Preprocessing `part` takes $O(m)$ time, while the matching step requires $O(n)$ time to complete. The space complexity is also $O(m+n)$, due to `lps` and `stack`.  
  

