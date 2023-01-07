## 1833. (M) Maximum Ice Cream Bars

### `solution.py`
We want to buy as many ice cream bars with a given budget, so the strategy of buying the cheapest bars first is always optimal. To do this, we first sort the supplied price list in ascending order and simply iterate over it until our budget is exhausted.  
  
#### Conclusion
The initial sort takes $O(n\log n)$ time and is the dominant factor. The space complexity is $O(n)$ since the sort is performed in-place.  
Not really sure why this problem is labeled as medium... it doesn't make sense even as a trick question since problems aren't going to be labeled during interviews.
  
