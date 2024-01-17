## 1207. (E) Unique Number of Occurrences

### `solution.py`
The most straightforward method of solving this problem is to simply count the number of occurrences for each unique value, then determining whether all of those values are unique. We can easily solve this with a dictionary and a set, where the dictionary is used to keep track of the frequency count of each unique value and the set is used to identify the unique values among those frequency counts. We first initialize a `Counter` passing `arr` as the argument. The resulting object `freq` will contain key-value pairs where the keys are the unique values in `arr` and the values the number of occurrences of that value in `arr`. We then initialize a set passing the values of `freq` as the argument. The contents of the resulting object `freq_set` will be the unique number of occurrences in `freq`. As we want to verify whether all unique values in `arr` also appear in `arr` a unique number of times, it stands to reason that the number of key-value pairs in `freq` (the number of unique values in `arr`) should equal the number of elements in `freq_set` (the number of unique occurrences of each unique value in `arr`) for this to be true. Thus, we can simply compare the size of `freq` and `freq_set` and directly return the result.  

#### Conclusion
The time complexity of this solution is $O(n)$ where $n$ is the length of `arr`. Initializing `freq` takes $O(n)$ as `arr` is iterated over exactly once with each element taking $O(1)$ time to process. Initializing `freq_set` also takes $O(n)$ time as `freq` can at most contain $n$ key-value pairs. The space complexity is $O(n)$ as well since `freq` and `freq_set` will use $O(n)$ memory each.  
  

