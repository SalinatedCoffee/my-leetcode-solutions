## 837. (M) New 21 Game

### `TLE.py`
The problem itself is a bit convoluted, so it may take some time to understand what the problem is asking. We are given three arguments `n`, `k`, and `maxScore`. A card is drawn which gives us a score in the range of `[1, maxScore]` where all scores have an equal probability of being rewarded. Cards are consecutively drawn until the total score is greater than or equal to `k`. We want the probability of the final score being at most `n` when the card drawing has completed. Before doing anything, we first need to work out how we should compute the probability for a given score. Say we are currently at some score `i`. We know that the game has not yet ended as we have drawn some card with score `j` to get to score `i`, and thus `i - j < k`. Naturally, getting to score `i` from score `i - j` has a probability of `1 / maxScore`. The maximum possible value of `j` can differ; it is either `i` itself (`j` was the first card of the game) or `maxScore`, whichever is lower. With this information, we see that we need to sum the probabilities for all possible values of `j` to compute the final probability for score `i`.  
First we initialize `dp`, a list of length `n + 1`. `dp[i]` will contain the probability of scoring score `i`, so we should initialize `dp[0]` to `1` since we start with a score of 0 100% of the time. Now we need to compute `dp[i]` for all values of `i`, which is in the range `[1, n]`. As established earlier, the value of `dp[i]` is the sum of `dp[i-j]` over all possible values of `j`, which is in the range `[1, min(maxScore, i)]`.  
Once `dp` has been populated, the answer we want is the sum of the subarray `dp[k:]` since we want the total probability of *finishing a game* scoring less than or equal to `n`.  

#### Conclusion
The time complexity of this solution is $O(n\cdot \text{maxScore})$ where $n$ is simply the parameter `n`. We iteratively populate `dp`, which is $n$ long, and each value of `dp` takes `maxScore` time. The space complexity is $O(n)$.  
  


### `solution.py`
The first solution, while correct, takes too long to run and will fail with TLE on test cases with large enough inputs. For each computation for `dp` we see that redundant computations occur computing the partial sum of the sliding window. Instead, we can keep the window sum stored in a variable (`s`) and update it as we move along.  

#### Conclusion
This solution has a time and space complexity of $O(n)$.  
  

