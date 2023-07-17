class Solution:
  def smallestSufficientTeam(self, req_skills: List[str], people: List[List[str]]) -> List[int]:
    # bottom-up dynamic programming with bit manipulation

    m = len(req_skills)
    n = len(people)
    stoi = {}
    for i in range(m):
      stoi[req_skills[i]] = i

    ptob = [0] * n
    for i in range(n):
      for skill in people[i]:
        ptob[i] |= 1 << stoi[skill]
    
    # dp[i] is bitmask of smallest team that possesses skill set represented by bitmask i
    dp = [2**n-1] * (2**m)
    dp[0] = 0

    for i in range(1, 2**m):
      for j in range(n):
        missing_skills = i & ~ptob[j]
        if missing_skills != i:
          team = dp[missing_skills] | (1 << j)
          if dp[i].bit_count() > team.bit_count():
            dp[i] = team
    
    # convert mask into list of integers
    ret = []
    idx = 0
    mask = dp[-1]
    while mask:
      if mask & 1:
        ret.append(idx)
      idx += 1
      mask >>= 1

    return ret

