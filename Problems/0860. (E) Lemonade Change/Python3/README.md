## 860. (E) Lemonade Change

### `solution.py`
A lemonade costs `5` dollars, and customers can pay for a single lemonade using either a `5`, `10`, or `20` dollar bill. When serving the line of customers that will each pay with `bills`(where the `i`th customer pays using `bills[i]`), we are asked to determine whether we can hand out the appropriate amount of change to each and every customer. If at any point in the line we cannot do so, we should return `False`.  
Thinking about the problem, we notice that we will ever only give out `5` and `10` dollar bills as change. We also realize that there is only 1 way to give out change for a `10` dollar bill, and 2 ways for a `20` dollar bill. While we serve customers while keeping track of the number of `5` and `10` dollar bills, we can easily determine whether we can give the customer back their change. If we do not have enough bills, we immediately return `False`.  

#### Conclusion
The time complexity of this solution is $O(n)$, where $n$ is the length of `bills`. The space complexity is $O(1)$.  
  

