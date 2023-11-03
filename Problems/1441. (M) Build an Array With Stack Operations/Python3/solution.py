class Solution:
  def buildArray(self, target: List[int], n: int) -> List[str]:
    # simulation

    PUSH, POP = "Push", "Pop"
    ret = []
    n_stream = 1
    for t in target:
      # extend ret by the number of data stream values to be discarded
      ret.extend([PUSH, POP]*(t - n_stream))
      n_stream = t
      ret.append(PUSH)
      n_stream += 1
    
    return ret

