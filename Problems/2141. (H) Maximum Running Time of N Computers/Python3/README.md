## 2141. (H) Maximum Running Time of N Computers

### `solution.py`
One thing to note is that we can let a computer drain a battery until it is empty. Batteries can be swapped in zero time, and as such we can keep a computer on past its battery's remaining charge if we switch to a fresh one *just* as the current one goes flat. This lets us effectively treat a pool of multiple batteries as one giant battery, which makes things easier for us.  
First, let's think about the trivial case where `n == len(batteries)`. Since all batteries are in use by a computer, the maximum running time would simply be `min(batteries)`. What if we were given one more battery, so `n + 1 == len(batteries)`?  

#### Conclusion
\<Content\>  


### `solution_2.py`
\<Content\>  

#### Conclusion
\<Content\>  
  

