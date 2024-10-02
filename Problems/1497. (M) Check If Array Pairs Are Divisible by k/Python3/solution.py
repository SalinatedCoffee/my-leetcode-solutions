class Solution:
  def canArrange(self, arr: List[int], k: int) -> bool:
    # modulo math with dictionary

    # mod each element by k and count frequency of values in the interval [0, k)
    freq = Counter([i % k for i in arr])
    # determine whether arr is pairable
    if freq[0] % 2:
      return False
    for i in range(1, k // 2 + 1):
      if freq[i] != freq[k-i]:
        return False

    return True

