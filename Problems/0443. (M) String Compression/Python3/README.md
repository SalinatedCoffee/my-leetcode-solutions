## 443. (M) String Compression

### `solution.py`
We want to compress the string in-place, which means that we need to overwrite items in `chars`. Iterating through `chars` we obviously can't just overwrite the items at the current location; instead we need to keep track of where we should overwrite next, so we can keep two pointers `cur_idx` and `end_idx` which contains the index of the current item and the first item that can be overwritten, respectively.  
Iterating through `chars` then we increment a counter whenever we encounter a letter identical to the one being counted, and overwrite elements starting at `end_idx` otherwise. We use a nested `for` loop to insert the string representation of `count` as we need to insert each digit separately.  
Once the `while` loop has exited we need to remember to insert the last group of characters as the insertion only takes place when it detects a letter change.  

#### Conclusion
This solution takes $O(n)$ time to run where $n$ is the length of `chars`. The space complexity is $O(1)$, as requested by the problem description.  
  

### `solution_2.py`
The first solution can be further optimized by consuming letters in groups. Instead of advancing by 1 and adding the compressed letters on a letter change, we can iterate over a run of consecutive letters, add the compressed string, and repeat until the end of `chars` is reached. This also eliminates the need for manually compressing the last group of letters as compression happens at the end of a letter group as opposed to the beginning of a new letter group.  
The nested `for` loop can also be replaced by a list assignment by slice, as assigning to a slice modifies the *list being sliced* rather than a copy of the slice. Slightly confusing considering the fact that slicing a list returns a copy of the sliced portion, but actually makes sense once you think about it for a while.  
  
#### Conclusion
The time and space complexity is the same as the first solution, but this one runs faster in practice (and is a lot cleaner) mostly thanks to the elimination of the nested `for` loop.  
  

