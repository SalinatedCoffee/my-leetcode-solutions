## 786. (M) K-th Smallest Prime Fraction

### `solution.py`
The most easiest method would be to simply generate all possible fractions and sort them by the actual value. Here we have opted for a min heap, which is exactly what we want since we are asked to return the `k`th *smallest* fraction. For each `i`th element of `arr`, where `i` is in the range `[0, n-1]`, we generate all possible fractions that have `arr[i]` as the numerator. For each fraction we push a tuple that contains the evaluated value of the integer(which is a float) and a list of length 2 where its values are the numerator and denominator of said fraction, in that order. Once all possible fractions have been pushed onto the heap, we pop from it `k - 1` times, after which the first item on the heap will contain the tuple that corresponds to the `k`th smallest fraction.  

#### Conclusion
The time complexity for this problem is $O(n^2\log n^2)$, where $n$ is the length of `arr`. Given a list of length $n$, there are $O(n^2)$ possible fractions. Because each and every fraction are pushed onto the heap, this step will take $O(n^2\log n^2)$ time to complete. The same can be said for the retrieval step since `k` is bound by $n^2$. The space complexity is $O(n^2)$ due to the heap.  
  


### `solution_2.py`
The previous solution can be further optimized by realizing that we can avoid having to push all possible fractions onto the heap and instead push and pop fractions at the same time.  
If the numerator of a fraction is the same, selecting the largest possible value for the denominator will yield the smallest fraction. In other words, if we select the largest value in `arr` as the denominator that fraction will be the smallest fraction among all other fractions that have the same numerator. Thus, we can generate a list of the smallest fraction for each numerator by dividing each value in `arr` with `arr[-1]`(since `arr` is already sorted in ascending order). We can also observe that given some fraction `arr[i] / arr[j]` the next smallest fraction that also has `arr[i]` as its numerator is simply `arr[i] / arr[j+1]`(if `j+1 < n`). By combining these observations with the behavior of a min heap, we can implement a faster solution based on the main idea of the previous solution.  
The previous solution generated all possible fractions and stored them in a min heap, after which `k - 1` items were popped from said heap to gain access to the `k`th smallest fraction. In this solution, we first push the smallest fraction for each numerator onto the heap and then pop items off of said heap, while pushing the next smallest fraction with the same numerator of the fraction that was just popped. Because the first item of the heap will always be the smallest stored item, this will guarantee that the fractions will be popped in ascending order of their values.  
We first populate the heap with the smallest fraction of each numerator by iterating over `arr` and dividing each value with `arr[-1]`. Then we pop an item off of the heap, after which we push the next smallest fraction with the same numerator as the fraction that was just popped off(if one exists). This is repeated `k - 1` times, after which the first item on the heap will be the `k`th smallest fraction overall.  

#### Conclusion
This solution has a time complexity of $O((n+k)\log n$, where $k$ is `k`. Initially populating the heap takes $O(n\log n)$ time, since $n$ fractions are pushed onto the heap. The following pop-push step takes $O(k\log n)$ time, since a pop-push pair of operations can happen $k$ times on a heap that can contain at most $n$ values. Hence, the overall time complexity is $O(n\log n + k\log n) = O((n+k)\log n)$. One could argue that $k$ is bound by $O(n^2)$, and thus the time complexity should be $O(n^3\log n)$, which is certainly true. However, this is a very loose bound as the maximum value of $k$ is actually $n(n-1) / 2$, and in practice will run faster than the previous solution. The space complexity is $O(n)$, due to the min heap.  
  


### `solution_3.py`
The follow up question asks us to implement a solution that runs faster than $O(n^2)$. This means that approaches based on enumerating all `k` smallest fractions are no longer viable, as `k` is bound by $n^2$. A drastically different approach is required, which can be   
  
#### Conclusion
  
  
  