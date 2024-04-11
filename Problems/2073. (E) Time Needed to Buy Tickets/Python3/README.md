## 2073. (E) Time Needed to Buy Tickets

### `solution.py`
As only the person at the front of the line can buy tickets, and returns to the back of the line if they still want to buy more tickets, we can solve this problem by using a stack. The number of tickets each person in line wants to buy is given to us as the list `tickets`, where `tickets[i]` is the number of tickets the `i`th(0-indexed) person wants to buy. We are asked to determine the amount of time required for the `k`th person to buy the number of tickets they want, where each ticket purchase takes 1 second.  
Without explicitly using a stack, we can instead simulate one by accessing `tickets` using a monotonically increasing index. While `tickets[k]` is not zero, we examine the person currently in front of the line, `tickets[idx]`. If they still want to purchase a ticket, we sell them one and increment the time elapsed by `1`. Otherwise, we simply move on to the next person in line. We also apply a modulus operation to `idx` to make sure it wraps back to the `0`th person after the `len(tickets)-1`th person is given a chance to buy a ticket.  

#### Conclusion
The time complexity of this solution is $O(mn)$ where $m$ is the value of `tickets[k]` and $n$ is the length of `tickets`. A single iteration over `tickets` decrements all of its values by `1`, which continues until `tickets[k]` becomes `0`. Hence, $n$ items will be iterated over $m$ times, bringing the overall time complexity to $O(mn)$. The space complexity is $O(1)$.  
  

