class Solution:
  def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    # greedy

    n = len(words)
    ret = []
    # list of current tokens
    cur = []
    # current number of spaces, current number of characters
    cur_pad, cur_char = 0, 0
    for i in range(n):
      w_len = len(words[i])
      w_pad = 0
      # if not first word add 1 char padding
      if cur_char:
        w_pad = 1
      # if adding current word would exceed max width
      if cur_pad + cur_char + w_pad + w_len > maxWidth:
        # if current line contains single word
        if not cur_pad:
          cur.append(" " * (maxWidth - cur_char))
        else:
          # determine base / extended padding
          avbl_space = maxWidth - cur_char
          base_pad = avbl_space // cur_pad
          ext_pad = avbl_space % cur_pad
          # stringify and pad space tokens
          pad = " " * base_pad
          j = 0
          while j < cur_pad:
            cur[j*2+1] = pad + " " if j < ext_pad else pad
            j += 1
        ret.append(''.join(cur))
        # prepare to process next line
        cur = []
        cur_pad, cur_char = 0, 0
        w_pad = 0
      # add current word to current line
      cur_pad += w_pad
      if w_pad:
        cur.append(' ')
      cur_char += w_len
      cur.append(words[i])
    # justify last line
    if cur:
      cur.append(" " * (maxWidth - cur_char - cur_pad))
      ret.append(''.join(cur))
    
    return ret

