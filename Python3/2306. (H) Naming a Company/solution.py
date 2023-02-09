class Solution:
  def distinctNames(self, ideas: List[str]) -> int:
    # group words based on prefix

    alph = string.ascii_lowercase
    # key: ideas[i][0], value: set(ideas[i][1:])
    prefix = {}
    for word in ideas:
      if word[0] not in prefix:
        prefix[word[0]] = set()
      prefix[word[0]].add(word[1:])

    res = 0
    # for every prefix pair
    for i in range(len(alph)):
      if alph[i] not in prefix:
        continue
      for j in range(i+1, len(alph)):
        if alph[j] not in prefix:
          continue
        s1 = prefix[alph[i]]
        s2 = prefix[alph[j]]
        intr = len(set.intersection(s1, s2))
        # count all valid suffix pairs w/ reversed order
        res += (len(s1)-intr)*(len(s2)-intr)*2

    return res

