## 213. (M) House Robber II

### `solution.py`
At first glance this problem may sound more complicated than it really is, as the circular array seems to imply that you would need to consider the `n-1`th and `n-2`th houses at the `0`th house. However the burglary run is happening in a single night, so we don't have to worry about wrapping around the array as stealing the `0`th house, moving through all houses, and stealing the `1`st house will still trigger the alarm. This simplifies the problem greatly since now we only need to consider two scenarios; when we steal from the first house, or when we don't steal from the first house. If we do steal from the first house we obviously can't steal from the last house and vice versa. Now it is simply a matter of applying [problem #198](../../0198.%20(M)%20House%20Robber/Python3/README.md) twice, on ranges `[0, n-2]` and `[1, n-1]`.  

#### Conclusion
This solution takes $O(n)$ time to run, where $n$ is the number of houses. The space complexity is $O(1)$.  
  


### `solution_2.py`
This solution is exactly the same as the first one, only written in a more compact fashion using two `for` loops.  

#### Conclusion
The solution has the same time and space complexity as the previous one.  
  