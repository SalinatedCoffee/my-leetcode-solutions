## 215. (M) Kth Largest Element in an Array

### `solution.py`

The trivial answer of course, is to simply sort `nums` in order to gain constant time access to the Kth largest value.  

#### Conclusion

The time complexity is $O(n\log n)$, where $n$ is the length of `nums`. `List.sort()` performs an in-place ascending sort which takes $O(n\log n)$ time. The space complexity is $O(n)$, since `List.sort()` uses $O(n)$ memory during runtime.  





### `solution_2.py`

The follow-up question is a bit ambiguous - it should be asking us to solve the problem without using *built-in* sort methods instead of *any sorting algorithms* whatsoever.  

Anyhow, we can use a modified version of [Quickselect](https://en.wikipedia.org/wiki/Quickselect) to solve this problem. Quickselect (and by extension, Quicksort) is based on selecting a random value as a pivot and segmenting the array into 3 parts; one that contains values smaller than the pivot, one that contains equal values, and one that contains larger values. We then choose between either the smaller or larger value array and recurse down it. Here we want the Kth largest value, so our choice will depend on where this value could be found.  

Say we have the larger, equal, and smaller elements (compared to the pivot) stored in lists `l`, `m`, and `r`, respectively. If `l` contains more elements than `k`, obviously the `k`th largest element must be in `l`. If there are *less* elements in `l` and `m` combined than `k`, the `k`th largest element must be in `r`. Otherwise the `k`th largest element is in `m`, which contains elements equal to the pivot.  

One thing to keep in mind is that we are essentially discarding `len(l) + len(m)` largest elements whenever we determine that our desired value is in `r`, and so we must correctly adjust `k` for the next recursive call on `r`. This is simply `k - (len(l) + len(m))`.  

#### Conclusion

The time complexity for this solution is $O(n)$, where $n$ is the length of `nums`. Quickselect has a worst case time complexity of $O(n^2)$, but has an average case TC of $O(n)$. This is due to the random nature in which pivots are selected. Given a reasonably large $n$, the probability of pivots being chosen in such a way that the algorithm runs in $O(n^2)$ is small enough to ignore. The space complexity is also $O(n)$, since `l`, `m` , and `r` use $O(n)$ memory, as well as the recursion stack.  





### `solution_3.py`

There is yet another approach that involves counting sort. Counting sort simply keeps track of the number of occurances for each element in an array (usually stored in a separate array) and later reconstructs a sorted array from that information. Here we only need to find the `k`th largest number, so we may skip the reconstruction step. We first need to determine the smallest and largest value in `nums` in order to initialize the counting array. Since `nums` only contains integers, it stands to reason that the contents of `nums` can be comprised of any number (inclusive) between `min_n` and `max_n` where `min_n` and `max_n` are the smallest and largest value in `nums`, respectively. Thus, the length of our counting array should be `max_n - min_n + 1`. During the counting step we realize that `nums` can also contain negative integers, which we clearly cannot use to index into `count`. We can sidestep this problem by shifting values to the right by `min_n`, which allows us to map negative values to its proper index in `count`.  

Once the counting has finished, we traverse `count` in reverse order while subtracting each element from `k`. Once `k` is less than or equal to `0`, it means that the current index of `count` is the `k`th largest number in `nums`.  

#### Conclusion

This solution has a time complexity of $O(n+k)$, where $k$ is the difference between the smallest and largest value in `nums`. `nums` is traversed multiple times, with each traversal taking $O(n)$ time. The initialization and traversal of `count` takes $O(k)$ time each, hence the overall time complexity of $O(n+k)$. The space complexity is $O(k)$.  




