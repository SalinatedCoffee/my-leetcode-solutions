class Solution:
  def countOfAtoms(self, formula: str) -> str:
    # stack with dictionaries

    n = len(formula)
    # contains counts of previously seen elements
    stack = [defaultdict(int)]
    idx = 0
    while idx < n:
      # prepare to count new set of elements
      if formula[idx] == '(':
        stack.append(defaultdict(int))
        idx += 1
      # merge current set of elements into outer set
      elif formula[idx] == ')':
        cur_cnt = stack.pop()
        idx += 1
        mul = ""
        # find and determine multiplier if it exists
        while idx < n and formula[idx].isdigit():
          mul += formula[idx]
          idx += 1
        # update counts of current set of elements
        if mul:
          mul = int(mul)
          for el in cur_cnt:
            cur_cnt[el] *= mul
        # merge counts into outer set
        for el in cur_cnt:
          stack[-1][el] += cur_cnt[el]
      # parse element symbol and update its count
      else:
        cur_el = formula[idx]
        idx += 1
        while idx < n and formula[idx].islower():
          cur_el += formula[idx]
          idx += 1
        cur_num = ""
        while idx < n and formula[idx].isdigit():
          cur_num += formula[idx]
          idx += 1
        if cur_num == "":
          stack[-1][cur_el] += 1
        else:
          stack[-1][cur_el] += int(cur_num)
    # sort elements in ascending order by symbol
    final_cnt = dict(sorted(stack[0].items()))
    # construct string representation of counts
    ret = ""
    for el in final_cnt:
      ret += el
      if final_cnt[el] > 1:
        ret += str(final_cnt[el])

    return ret

