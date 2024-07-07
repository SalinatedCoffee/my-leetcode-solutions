class Solution:
  def passThePillow(self, n: int, time: int) -> int:
    # modulo

    q, r = time // (n-1), time % (n-1)

    return n-r if q % 2 else r+1

