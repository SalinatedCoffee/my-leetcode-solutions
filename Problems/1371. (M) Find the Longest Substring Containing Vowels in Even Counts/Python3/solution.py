class Solution:
  def findTheLongestSubstring(self, s: str) -> int:
    # greedy algorithm using prefix counts

    n = len(s)
    ctoi = {'a':0, 'e':1, 'i':2, 'o':3, 'u':4}
    # generate prefix vowel count
    counts = []
    cur_counts = [True]*5
    for i in range(n):
      if s[i] in ctoi:
        cur_counts[ctoi[s[i]]] ^= True
      counts.append(cur_counts[:])
    counts.append([True]*5)

    # greedily determine length of longest substring
    for i in range(n, 0, -1):
      for j in range(0, n-i+1):
        even = True
        for k in range(5):
          if (counts[j+i-1][k] ^ counts[j-1][k]) is True:
            even = False
            break
        if even:
          return i
    
    return 0

