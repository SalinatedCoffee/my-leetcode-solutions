class Solution:
  def compress(self, chars: List[str]) -> int:
    # optimized two pointers

    # points to first unprocessed character
    cur_idx = 0
    end_idx = 0
    counting = chars[0]
    while cur_idx < len(chars):
      count = 1
      # count current group of characters
      while (cur_idx + count < len(chars) and
             chars[cur_idx + count] == chars[cur_idx]):
        count += 1
      # append letter being counted to end of compressed string
      chars[end_idx] = chars[cur_idx]
      end_idx += 1
      # append letter count to end of previous
      if count > 1:
        str_count = str(count)
        # python list assignment
        chars[end_idx:end_idx+len(str_count)] = list(str_count)
        end_idx += len(str_count)
      # advance current index
      cur_idx += count

    return end_idx

