class Solution:
  def findCenter(self, edges: List[List[int]]) -> int:
    # dictionary

    # flatten list of edges and count occurrance of each node value
    # the list comprehension decomposed into for loops looks like this:
    # for edge in edges:
    #   for i in edge:
    #     freq.append(i)
    freq = Counter([i for edge in edges for i in edge])

    # TIL max() has a key argument
    return max(freq.keys(), key=lambda x: freq[x])

