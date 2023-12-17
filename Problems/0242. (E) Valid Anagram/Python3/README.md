## 242. (E) Valid Anagram

### `solution.py`
In order to check whether `t` is an anagram of `s`, we need the frequency count of all characters in both strings. For this problem, the alphabet only consists of the lower case english letters, of which there are 26 of. Because the alphabet is small we can simply store the frequency of each letter in a list, where the `0`th element is the count of `a`, the `1`st element the count of `b`, and so on. We populate a list for both `t` and `s`, and compare the frequency of each letter. If a mismatch is found, `t` cannot possibly be an anagram of `s`, and so we immediately return `False`. Otherwise the loop exits normally, and we return `True`.  

#### Conclusion
This solution has a time complexity of $O(m+n)$, where $m$ and $n$ are the length of `s` and `t`, respectively. Each string is iterated over once to count the frequency of each unique letter. The space complexity is $O(1)$, since for each string we keep a list of length 26 in memory.  
  


### `solution_2.py`
The follow up question asks us to consider the case where the alphabet consists of all Unicode letters. In this scenario, the previous approach becomes very inefficient - as of this post, there are [149,878](https://en.wikipedia.org/wiki/List_of_Unicode_characters) characters in Unicode which means that we would have to initialize 2 lists of length 149,878 even when comparing very short strings. Instead, we can switch to using dictionaries. Python dictionaries allows us fast access to a key's value, and on top of that we only have to store the relevant characters in memory, greatly reducing the required space.  
We initialize a `defaultdict(int)` for `t` and `s`. The key will be the character, and the value will be the number of occurances of that character in its string. We also initialize a set `chars`, which will contain the characters in *both* `t` and `s`. This is to prevent false positives where `t` is a subset of `s` and vice versa, such as `s = abcd, t = abc`. Now we iterate over `t` and `s`, while counting the number of occurances of each unique character. Once this is complete we use `chars` to retrieve the value in each dictionary, and compare the values for every character in `chars`. Whenever a mismatch is found, we immediately return `False`. If the loop exits normally, we return `True`.  

#### Conclusion
The time complexity is identical to the first solution. The space complexity is $O(\text{max}(m+n, k))$, where $k$ is the size of the alphabet.  
  

