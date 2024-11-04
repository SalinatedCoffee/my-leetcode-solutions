class Solution:
  def compressedString(self, word: str) -> str:
    # implementation

    # build answer in list to avoid string operations
    res = []
    cur_letter, cur_count = word[0], 0
    for c in word:
      if c != cur_letter:
        res.extend([str(cur_count), cur_letter])
        cur_letter, cur_count = c, 0
      elif cur_count == 9:
        res.extend([str(cur_count), cur_letter])
        cur_count = 0
      cur_count += 1

    res.extend([str(cur_count), cur_letter])

    return ''.join(res)

