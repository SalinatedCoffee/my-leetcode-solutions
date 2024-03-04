## 948. (M) Bag of Tokens

### `solution.py`
At first glance, the problem looks like a dynamic programming problem. Upon further inspection however it becomes clear that it is not, mainly because we can play tokens in any order we want. Since a DP-based approach is now out of the question, the next logical step would be to see if we can devise a greedy algorithm based approach.  
Returning to the problem description, there are 2 possible plays that we can make if we decide to play some token `tokens[i]`. We can either spend `1` score and increase our power by `tokens[i]`, or we can spend `tokens[i]` power and increase our score by `1`. Since we are asked to maximize the *score*, we obviously want to increase the score as many times as possible. Since the only way to increase the score is by spending power, we would want to consequently increase our score by using the minimum amount of power necessary. As mentioned previously, we can play tokens in any order; hence, we can sort `tokens` in ascending order (or vice versa) to greedily play each token based on their values.  
We first sort `tokens` in ascending order. Then we initialize two indices, each pointing to the unplayed token with the smallest / largest value. Because we start off with a score of `0`, we first check whether we have enough power to play the smallest token and increase our score. If not, we check if we have a non-zero score to play the largest token to gain more power. These checks are repeated until either all tokens have been played or we do not have enough score or power to play. For the latter, we simply return the current score. For the former, we do a last check to see if we have enough power to play the last token, and return the appropriate score.  

#### Conclusion
This solution has a time complexity of $O(n\log n)$, where $n$ is the length of `tokens`. Sorting `tokens` takes $O(n\log n)$ time to complete, outscaling the playing step that has a time complexity of $O(n)$. The space complexity is $O(n)$, also due to the initial sorting step.  
  

