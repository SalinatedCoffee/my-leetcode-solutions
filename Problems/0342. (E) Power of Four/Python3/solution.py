class Solution:
  def isPowerOfFour(self, n: int) -> bool:
    # modulo operation

    # sanity check
    if n <= 0:
      return False
   
    while n > 1:
      n, r = n // 4, n % 4
      if r != 0:
        return False

    return True

