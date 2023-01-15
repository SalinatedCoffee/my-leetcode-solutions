class Solution:
  def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
    # group equivalent characters
    # python sets support set operations (disjoint, union, intersection, etc)
    # but that feels like cheating so we'll do it using union find
    # lexicographically smaller letters have higher rank

    # initialize initial nodes
    p = {c: c for c in string.ascii_lowercase}
    
    def ufind(a):
      pa = p[a]
      # recurse until parent node is self (set representative)
      if pa != a:
        p[a] = ufind(pa)
      return p[a]

    def uunion(a, b):
      # get lex. smallest letter of sets
      pa, pb = ufind(a), ufind(b)
      # merge sets based on rank
      if pa > pb:
        p[pa] = pb
      elif pb > pa:
        p[pb] = pa

    # perform set union on letter pair for all pairs
    for a, b in zip(s1, s2):
      uunion(a, b)

    # generate transformed baseStr
    return "".join(ufind(c) for c in baseStr)

