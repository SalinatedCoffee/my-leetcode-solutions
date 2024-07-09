## 1701. (M) Average Waiting Time

### `solution.py`
Given a list of tuples `customers`, we are asked to determine the average waiting time of all customers. `customers[i]` is a tuple where `customers[i][0]` is the time at which the customer arrives and `customers[i][1]` is the time required to prepare that customers order. There is a single chef that process the orders one at a time. The most straightforward approach would be to simulate the problem, since `customers` is already conveniently sorted in ascending order of arrival time. In order to determine the average waiting time, we need to know the time at which the chef will finish working on an order and the sum of the time that all previous customers have had to wait. If the chef is busy when a customer arrives, that customer has to first wait for the chef to finish whatever they were doing and then wait until their order is fulfilled. The former is simply the 'time-until-chef-idle' subtracted by the time the customer arrives, and the latter is the time it takes to prepare the customer's order. If the chef is already idle, they can immediately start working on the customer's order, leading to a wait time consisting of only the latter. In both cases the required time is trivial to compute, and we do so for each and every tuple in `customer`. Now that we know the total time that the customers have had to wait, we can easily compute the average by dividing that value by the total number of customers.  

#### Conclusion
This solution has a time complexity of $O(n)$ where $n$ is the length of `customers`. `customers` is iterated over exactly once, and since each element takes $O(1)$ time to process the overall time complexity comes out to be $O(n)$. The space complexity is $O(1)$.  
  

