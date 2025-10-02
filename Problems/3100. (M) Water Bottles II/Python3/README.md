## 3100. (M) Water Bottles II

### `solution.py`
Given the integers `numBottles` and `numExchange`, we are asked to return the maximum number of water bottles we can drink when we are allowed to perform the following operations:  
- Drink from any number of water bottles, up to `numBottles`. Drinking from a water bottle turns it into an empty bottle.
- Exchange `numExchange` empty bottles for 1 water bottle. After the exchange, `numExchange` increases by 1. Exchanges cannot be 'bundled'; for example, you are not allowed to exchange 6 empty bottles for 2 water bottles when `numExchange = 3`.
We can easily solve this problem through simulation since the order of operations does not affect the end result. As we run through a loop, we drink all available water bottles and then attempt to exchange empty bottles whenever possible. If there are no water bottles left to drink from, and we are unable to exchange empty bottles, there is nothing left to do and so we return the total number of consumed water bottles.  

#### Conclusion
This solution has a time complexity of $O(\sqrt n)$, where $n$ is the value of `numBottles`. The space complexity is $O(1)$.  
  

