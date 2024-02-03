class Solution:
  def evalRPN(self, tokens: List[str]) -> int:
    # stack

    vals = []
    for t in tokens:
      if t in "+-*/":
        b, a = vals.pop(), vals.pop()
        match t:
          case "+":
            vals.append(a + b)
          case "-":
            vals.append(a - b)
          case "*":
            vals.append(a * b)
          case "/":
            vals.append(int(a / b))
      else:
        vals.append(int(t))

    return vals[0]

