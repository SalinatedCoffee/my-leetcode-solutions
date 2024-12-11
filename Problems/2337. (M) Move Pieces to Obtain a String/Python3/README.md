## 2337. (M) Move Pieces to Obtain a String

### `solution.py`
A given string can contain the 3 characters `L`, `R`, and `_`. These characters can be moved within the string while following these rules:  

- A `_` represents an empty space.  
- `L`s can be shifted towards the left by 1 character if there is an empty space.  
- `R`s can be shifted towards the right by 1 character if there is an empty space.  

Given these rules and the strings `start` and `target`, our task is to determine whether `target` can be formed by shifting the contents of `start` any number of times.  
First off, we can immediately see that the order of the non-empty characters in `start` must be identical to that of `target` for the pair of strings to be 'valid'(`target` can be formed by shifting characters in `start`). However, we cannot walk over both strings and naively match characters as each type of character can only be shifted in one direction. Example 3 is a perfect depiction of this problem; if we were to simply match non-empty characters in both strings, we would say that the two strings are valid. In reality, `_R` cannot be shifted to form `R_` since `R`s can only be moved towards the right.  
Returning to our first observation, we know that the relative order of non-empty characters in both strings must match for them to be valid. We also know that we can shift `L`s only towards the left, and `R`s to the right. This means that if we know the characters in each string that correspond to each other in this relative ordering, we can check whether the character can be moved to the position in `target` starting at the position in `start`. If `start[i]` and `target[j]` are `L`s, `i` **must be** greater than or equal to `j` for the pair to be valid. The same logic can be used for `R`s, where the pair is valid only if `i <= j` evaluates to true. Thus, we can walk over both strings while matching non-empty characters from each string against each other, checking their indices to determine whether all matched pairs are valid. If so, `target` can be formed by moving the contents of `start`, and we return `True`. Otherwise, we immediately return `False`.  

#### Conclusion
This solution has a time complexity of $O(n+m)$, where $n$ and $m$ are the lengths of the given strings `start` and `target`. Each string is effectively iterated over at most once, with each character taking $O(1)$ time to process. The space complexity is $O(1)$.  
  

