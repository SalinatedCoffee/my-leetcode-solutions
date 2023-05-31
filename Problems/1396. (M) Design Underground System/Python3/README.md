## 1396. (M) Design Underground System

### `solution.py`
Reading through the problem, it seems that we will be performing a lot of random access operations on the stored data - which means that we should be using dictionaries (also known as hash tables) in our solution. We declare two dictionaries as instance variables, where we store customer data in one and station data in the other. The customer dictionary is straightforward - we only need to store the check-in station and the timestamp for the customer's ID. For stations however there can be itineraries with different origin stations that end at the same station, and so we need to use a data structure that can offer fast access to the statistics given the origin station name. This can also be achieved with dictionaries, which we can nest inside the station dictionary we instantiated earlier. We can then simply keep track of the sum of all trip durations and number of passengers, and return the average whenever a valid call to `getAverageTime()` occurs.  

#### Conclusion
Instantiating `UndergroundSystem` takes $O(1)$ time. Calls to `checkIn()`, `checkOut()`, and `getAverageTime()` will also take $O(1)$ time, since all operations that take place take constant time due to the use of dictionaries. The space complexity is $O(i+j)$, where $i$ is the maximum number of customers checked in at a time and $j$ is the number of unique itineraries over the lifecycle of the object.  
  

