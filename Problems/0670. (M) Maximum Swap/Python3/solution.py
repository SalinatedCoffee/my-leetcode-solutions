class Solution:
  def maximumSwap(self, num: int) -> int:
    # brute force
    
    num_digits = [c for c in str(num)]
    n = len(num_digits)
    for i in range(n):
      max_digit = i
      # find the largest digit to the right of num_digits[i]
      #   that is larger than num_digits[i]
      for j in range(i+1, n):
        if num_digits[max_digit] <= num_digits[j]:
          max_digit = j
      if num_digits[max_digit] != num_digits[i]:
        num_digits[max_digit], num_digits[i] = num_digits[i], num_digits[max_digit]
        return int(''.join(num_digits))

    return num

