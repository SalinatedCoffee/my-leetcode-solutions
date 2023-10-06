## 229. (M) Majority Element II

### `solution.py`
The linear space solution is trivial to implement, where we count the frequence of each value in `nums` after which we simply return the values that appear more than `len(nums) // 3` times.  

#### Conclusion
This solution has a time and space complexity of $O(n)$, where $n$ is the length of `nums`.  
  

### `solution_2.py`
A solution that satisfies the follow-up question's request is much more interesting (and difficult). First off, since a number has to appear *more* than `len(nums) // 3` times to be considered a majority we know that there can at most be 2 such values. We can think of these values as soldiers, where different values 'fight' each other after which the values disappear. The values that 'survive' after processing the entierety of `nums` will be the majority values we want. Since there can be 2 majority values, for each value that participates in a fight, 2 other values will disappear.  
We keep track of 4 values; the candidate majority values, and their corresponding counters. While traversing `nums`, we perform the following for each value `i`:  

* If `i` is one of the candidates, we increment the counter for the candidate.  
* Otherwise, if either candidate has a counter value of `0`, `i` takes the place of that candidate and the counter is reset to `1`.  
* Otherwise, `i` is not a candidate and the counter for each candidate is non-zero, so decrement both counters by `1`.  

Once `nums` has been traversed, we now have the 2 'surviving' values of `nums`. However this does not guarantee that these values are the majority, and thus we need to traverse `nums` one more time to verify whether they appear more than `len(nums) // 3` times in `nums`.  

#### Conclusion
The time complexity of this solution is $O(n)$, and the space complexity is $O(1)$.  
The algorithm used here is known as the [Boyer-Moore majority vote algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm), which is quite frankly, a very niche algorithm that is also complex enough to render it unrealistic for your average interviewee to come up with in a typical interview setting.  
  

