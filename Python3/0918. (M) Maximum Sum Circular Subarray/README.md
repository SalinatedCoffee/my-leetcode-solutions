## 918. (M) Maximum Sum Circular Subarray

### `TLE.py`
We already know how to compute the maximum sum of a subarray in a given array using [Kadane's algorithm](https://en.wikipedia.org/wiki/Maximum_subarray_problem). A naive way of solving this problem is to simply run this algorithm starting from all indicies from `0` to `n-1`.  

#### Conclusion
This algorithm runs in $O(n^2)$ time and uses $O(1)$ space. While correct, it takes too long to run and TLEs test cases with large inputs.  
  

### `solution.py`
A subarray can be either a 'normal' subarray which does not wrap around the end of the array or a subarray that extends beyond the end of the array and wraps around to the start of it. In the first case we can trivially compute the value with the aformentioned Kadane's algorithm. The second case is where things get interesting. Intuition tells that if we split a subarray(that has the largest sum) in half, the two halves will also have the largest sums within their respective intervals while starting / ending at the position of the split. We can apply this to the wrap-around case by applying the split at the end of the array. Reversing from the end of the array, we can precompute the largest sum of all subarrays starting at some location `i` and ending at `n-1`. To achieve this we simply keep a rolling sum of all elements moving through the array in reverse order, and keep track of the maximum sum as necessary. Now we do the same for subarrays starting at index `0`, but this time taking into account the previously computed values we can compute the maximum sum of both subarrays of intervals `[0, i]` and `[i+1, n-1]`. As explained earlier this takes care of the case where a max sum subarray wraps around the end of the array, and thus we can compare the two values from the algorithm that was just explained and Kadane's algorithm returning the one that is larger.  

#### Conclusion
Kadane's algorithm runs in $O(n)$ time, and the 'wrap-around' algorithm takes $O(2n)$ time. Thus, this solution overall has a time complexity of $O(n)$ time, using $O(n)$ space for `dp` which holds the precomputed maximum sum of subarrays starting at `i` and ending at `n-1`.
  

### `solution_2.py`
A more efficient method exists that extends upon the idea of the first solution. We previously computed the maximum sum for the `wrap-around` case by thinking of it as finding the maximum sum of two subarrays with intervals of `[0, i]` and `[i+1, n-1]`. In reality, a third subarray between the two was abstracted out since we were only interested in finding the maximum sum and not the actual intervals of the subarrays. We can then reason that whenever the sum of the two subarrays are maximized, we also minimize the sum of the middle subarray since it is simply the total sum of the entire array subtracted by the sum of the two subarrays. The minimum sum of the middle subarray (which it turns out is a 'normal' subarray discussed in the first solution) can be trivially computed by modifying Kadane's algorithm. Thus we can correctly compute the desired value by iterating through the array once and comparing the sums from Kadane's algorithm and the 'normal minimum' algorithm.  
One thing to note is that there are a few edge cases that involve a scenario where all elements are negative, but this can be trivially checked for after the 'normal' sum and minimums are computed.  
  
#### Conclusion
The previous solution already ran in optimal time ( $O(n)$), as does this solution. However this solution uses $O(1)$ space by forgoing the list of precomputed max value of `[i, n-1]` subarrays.  
  

