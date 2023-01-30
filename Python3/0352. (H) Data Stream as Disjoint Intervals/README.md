## 352. (H) Data Stream as Disjoint Intervals

### `solution.py`
This would be a relatively easier problem to solve if Python had a built-in data structure that supports optimal inserts / deletes while guaranteeing that the contents are sorted (`heapq` *almost* satisfies these conditions) but it doesn't, and for problems like these I would rather avoid using external libraries whenever possible. One admittedly 'brute-force' way of tackling this problem is noticing that the input range is rather small - sufficiently small enough to just keep all values in memory.  
`addNum()` simply sets the value of `self._intervals[value]` to 1, and updates `self._min` and `self._max` accordingly. The min / max values are tracked so that we can avoid traversing the entirety of `self._intervals` for `every` call to `getIntervals()`.  
`getIntervals()` is also very simple. It simply iterates through values in range `[self._min, self._max]` and appending the previously seen interval to a return list whenever it encounters a `0` in `self._intervals`.  

#### Conclusion
`SummaryRanges` overall uses $O(1)$ space, but this is slightly misleading because it scales in terms of the size of whatever data type `value` is instead of the number of inputs. `addNum()` takes $O(1)$ time, and `getIntervals()` takes $O(n)$ time.  
'Why not use `bool`s instead of `int`s to save space?' is a good question - the snarky answer is that you probably shouldn't be using Python if you need that level of granularity in optimizing your code; the actual answer is that (without getting into too much technical detail) Python `int`s and `bool`s use the same amount of memory. You can verify this yourself with `sys.getsizeof()`. This is because Python internally uses a single instance of `True` and `False`, and when a variable is assigned one of these values it gets assigned the *memory address* of the canonical instance instead of the actual value.  
Obviously, this solution doesn't scale well to the range of `values`. It may be worth revisiting this problem and try to come up with a solution that *does* scale well in that regard.  

