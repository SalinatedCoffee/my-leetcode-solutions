## 2125. (M) Number of Laser Beams in a Bank

### `solution.py`
A security device can only emit a beam between another security device, if they are not on the same row and the rows between them do not contain any other security devices. In other words, a device can only form a beam between other devices in the nearest row. A device cannot emit multiple beams between the same device, but can emit a single beam between multiple devices. Using this property, we can compute the number of beams between two rows by multiplying the number of devices in each row.  
Now we can count the total number of beams in `bank`, by maintaining two integers. One will hold the number of devices in the last non-empty row, and the other will contain the number of devices of the current row. We examine `bank` row by row, counting the number of devices for each row. If the current row has no devices, we simply move on to the next row and repeat. Otherwise we add the product of the device count of the current row and that of the last non-empty row, then assign the current count to the last before resetting the current row count to `0`. Once all rows have been examined we simply return the total number of beams, which is stored in `ret`.  

#### Conclusion
This solution has a time complexity of $O(mn)$, where $m$ and $n$ are the dimensions of `bank`. Every element in `bank` is examined exactly once, with each operation taking $O(1)$ time to perform. The space complexity is $O(1)$, as we only use a handful of variables of primitive data types.  
  

