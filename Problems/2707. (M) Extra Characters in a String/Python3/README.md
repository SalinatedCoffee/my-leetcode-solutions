## 2707. (M) Extra Characters in a String

### `solution.py`
We can immediately recognize this as a dynamic programming problem, where we can build upon the results of a smaller subproblem. Here, if we know the mininum extra characters for the substring `s[:i]`, we can choose to consider the character `s[i]` as extra and move on. If there is a matching word in `dictionary` that starts with `s[i]` having length `k`, we can skip over `k` characters ahead and move on to `s[i+k]`. The problem here is that there is no simple way to determine whether there exists a matching word that starts with `s[i]`. We could convert `dictionary` into a set and try looking for all strings starting with `s[i]` in `s[i:]`, but hashing a string is a linear-time operation and will add an extra order of `len(s)` to the overall time complexity. Instead, we can convert the dictionary into a trie which will allow us to detect **all** matching words in linear time. Then, whenever a word is matched we can easily recurse on the appropriate index using optimal time.  
We first implement a simple `TrieNode` class which contains `self.c`, a dictionary of its children and `self.end`, a boolean which signifies whether the current node corresponds to the end of a word. A root node is instantiated, after which all words in `dictionary` is inserted into the root. Then, we define a recursive function `recurse()`, where `recurse(i)` will return the minimum number of extra characters in the substring `s[i:]`. As explained earlier, we have multiple choices at index `i`. We can count `s[i]` as extra, which means we add `1` to the result of `recurse(i+1)`. Or, we can try taking whichever matching word beginning with `s[i]`. Starting from the root, we descend down the dictionary trie while checking for any matches. If at any point in time a child trie node does not exist it means that any further matches are impossible, and we immediately exit. If a node's `TrieNode.end()` is `True`, it means that a match has been found and we update `ret` with `recurse(i+k+1)`, if it is smaller (`k` is the length of the matched word). The base case is when `i == len(s)`, since there are no more characters left to consider.  
By definition, we want the value of `recurse(0)`, which we can immediately return.  

#### Conclusion
The time complexity of this solution is $O(n^2+mk)$, where $n$ is the length of `s`, $k$ is the average length of a word, and $m$ is the length of `dictionary`. The recurrence relation has $n+1$ states, and computing each state takes $O(n)$ time since for some state `i` we check whether the substring `s[i:]` contains any matching words in the dictionary. Inserting a word of length `j` into a trie takes $O(j)$ time. Here we insert every word in `dictionary` into a trie, which takes $O(mk)$ time. The space complexity is $O(n+mk)$, since the `dictionary` trie uses $O(mk)$ memory and the recursion depth can at most be $n+1$ deep.  
  
