class Solution:
  def compress(self, chars: List[str]) -> int:
    # two pointers

    # points to first unprocessed character
    end_idx = 0
    cur_idx = 0
    counting = chars[0]
    count = 0
    while cur_idx < len(chars):
      if chars[cur_idx] == counting:
        count += 1
      else:
        if count > 1:
          chars[end_idx] = counting
          end_idx += 1
          for c in str(count):
            chars[end_idx] = c
            end_idx += 1
        else:
          chars[end_idx] = counting
          end_idx += 1
        counting = chars[cur_idx]
        count = 1
      cur_idx += 1

    # compress last character group
    if count > 1:
      chars[end_idx] = counting
      end_idx += 1
      for c in str(count):
        chars[end_idx] = c
        end_idx += 1
    else:
      chars[end_idx] = counting
      end_idx += 1
    
    return end_idx

