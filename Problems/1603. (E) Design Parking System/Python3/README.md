## 1603. (E) Design Parking System

### `solution.py`

We simply need to decrement the appropriate counter whenever `addCar()` is called. This can be implemented in multiple ways, but we have used the switch-case pattern for this solution.  



#### Conclusion

Instantiation of `ParkingSystem` and calls to `addCar()` have a time complexity of $O(1)$. The overall space complexity of `ParkingSystem` is also $O(1)$.  


