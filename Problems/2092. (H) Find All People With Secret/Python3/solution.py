class Solution:
  def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
    # union find

    p = [i for i in range(n)]

    def ufind(a):
      while p[a] != a:
        a = p[a]
      return a
    
    def uunion(a, b):
      pa, pb = ufind(a), ufind(b)
      if pa > pb:
        p[pa] = pb
      else:
        p[pb] = pa
    
    # give firstPerson the secret
    uunion(0, firstPerson)

    # group meetings by time
    g_meetings = defaultdict(list)
    for a, b, t in meetings:
      g_meetings[t].append((a, b))

    for i in sorted(g_meetings.keys()):
      # set of people that had a meeting at time i
      people = set()
      for a, b in g_meetings[i]:
        uunion(a, b)
        people.update([a, b])
      # if a person doesn't have the secret, 'reset' meeting that person was in
      for person in people:
        if ufind(person) != 0:
          p[person] = person

    ret = []
    for i in range(n):
      if ufind(i) == 0:
        ret.append(i)

    return ret

