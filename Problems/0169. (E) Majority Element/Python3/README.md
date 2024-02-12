## 169. (E) Majority Element

### `solution.py`
An easy solution is to simply count the number of each unique elements in `nums` and return the value with the highest frequency. We use a `Counter` to populate a dictionary with the frequency counts, after which we iterate over all key-value pairs and find the element with the highest frequency count.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `nums`. `nums` is iterated over once, and `freq` can at most contain $\lfloor n/2\rfloor$ items. The space complexity is also $O(n)$.  
  


### `solution_2.py`
The follow-up asks us to implement a solution that runs in linear time and uses constant space. In order to achieve this we need to resort to a rather niche algorithm known as the [Boyer-Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm). Essentially, the algorithm finds the majority element in an array of `n` items that contains some element that appears more than `n // 2` times. As a majority element is guaranteed to exist in every input array, we can use this algorithm to find the desired value.  

#### Conclusion
The time complexity of this solution is $O(n)$, and the space complexity is $O(1)$.  
  

