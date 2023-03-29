## 983. (M) Minimum Cost For Tickets

### `solution.py`
Intuition tells us that we can use dynamic programming here since the cost of a certain day depends on the costs of the previous days. To get to `days[i]`, there are three cases that could have happened to get to that index. The 1-day ticket case is trivial, as we only could have purchased a ticket at `days[i-1]`. For the other two tickets, we need to look back in `days` and find the earliest index (say, `j`) that contains a value where the difference between it and `days[i-1]` is less than 7 (or 30, for the 30-day ticket). Then, if the total cost of purchasing the 7-day ticket `dp[j]+costs[1]` is smaller than the current cheapest cost to reach `days[i]` (that is, `dp[i]`) we purchase the ticket.  

#### Conclusion
The time and space complexity is $O(n)$ where $n$ is the length of `days`.  
One thing to remember is that the running time is technically $O(37n)$ since we look back 37 days for each element in `days`. Since this constant is meaningfully large compared to $n$($n$ can be at most 365 per the problem constraints), the asymptotic worst case should be taken with a grain of salt.  

