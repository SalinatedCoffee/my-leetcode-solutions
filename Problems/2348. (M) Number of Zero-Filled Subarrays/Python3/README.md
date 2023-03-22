## 2348. (M) Number of Zero-Filled Subarrays

### `solution.py`
We want the total number of *subarrays*, so we only need to consider consecutive runs of `0`s. To count the number of all possible subarrays given an array of length `n` then, we can first start by considering subarrays of length 1. The number is simply `n`, for obvious reasons. Moving on to subarrays of length 2, the count is `n-1`. We can reason about this by treating the subarrays as a 'sliding window' that moves along the array. For example, if the array has a length of 5, the subarrays can contain the first and second elements, the second and third elements, the third and fourth elements, and finally, the fourth and last elements. Generalizing this to arrays of any size we realize that we can compute the number of all subarrays with the formula $n(n+1) / 2$ (Gauss summation).  
Using this formula the implementation becomes trivial.  

#### Conclusion
The time complexity is $O(n)$ where $n$ is the length of `nums`. The space complexity is $O(1)$.  
  

