## 1518. (E) Water Bottles

### `solution.py`
`numExchange` empty bottles can be exchanged for a single full bottle. When initially given `numBottles` full bottles, we are asked to return the maximum number of full bottles that can be consumed. Since there is no closed form formula that can be evaluated to determine this value, we must simulate the process instead. We initialize 2 aptly named integers `full` and `empty`. While the sum of `full` and `empty` is larger than `numExchange`, we first drink `full` bottles, adding the number to the sum `ret` and `empty`. We then exchange the empty bottles for full bottles by evaluating the expression `empty // numExchange`. Whatever empty bottles we have left over is stored in `empty` by computing `empty % numExchange`. When the loop exits we simply return `ret + full`, since there may still be full bottles that are left over.  

#### Conclusion
This solution has a time complexity of $O(\log_m n)$ where $n$ is `numBottles` and `numExchange` is $m$.  
  

