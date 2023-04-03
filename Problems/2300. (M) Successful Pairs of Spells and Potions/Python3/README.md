## 2300. (M) Successful Pairs of Spells and Potions

### `solution.py`
A brute-force solution involves manually trying all pairs of spells and potions, and will take too long. We can instead sort `potions`, after which we may perform a binary search. Iterating through `spells`, we search for the last element that forms a successful pair. Then the number of desired pairs is simply the length of `potions` subtracted by the index of the element we searched for earlier.  
Note that this approach also works when the search is performed on `spells` instead of `potions`.  

#### Conclusion
This solution has a time complexity of $O(n\log m + m\log m) = O((n+m)\log m)$ where $n$ is the length of `spells` and $m$ is the length of `potions`. Sorting `potions` takes $O(m\log m)$ time, and binary search takes $O(\log m)$ time which is performed $n$ times. The space complexity is $O(1)$ since the sort is performed in-place.  
  

### `solution_2.py`
We can take a different approach, where we trade off memory for speed. If we sort both `spells` and `potions`, then successful pairs for `spells[i]` will also be successful for `spells[i+1]`. Using this we can maintain a pointer to the last successful potion for the previous spell, and start iterating from there instead of looking through the entirety of `potions` every time.  
One thing to remember is that the return list should contain the number of pairs in the original order of `spells`, and so we need to preserve the original indices of the spells when sorting it.  

#### Conclusion
The time complexity is $O(n\log n + m\log m + n + m$) since `spells` and `potions` are each sorted and traversed once. The space complexity is $O(n)$ as we store an additional integer for each element in `spells`.  
  
