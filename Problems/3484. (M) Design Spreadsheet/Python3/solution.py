class Spreadsheet:
  # dictionaries
  
  def __init__(self, rows: int):
    # sparsely store values
    self._sheet = {col: defaultdict(int) for col in string.ascii_uppercase}

  def setCell(self, cell: str, value: int) -> None:
    col, row = cell[0], cell[1:]
    self._sheet[col][row] = value

  def resetCell(self, cell: str) -> None:
    col, row = cell[0], cell[1:]
    if row in self._sheet[col]:
      del self._sheet[col][row]

  def getValue(self, formula: str) -> int:
    # naively parse formula string
    a, b = formula[1:].split('+')
    a = int(a) if a.isnumeric() else self._sheet[a[0]][a[1:]]
    b = int(b) if b.isnumeric() else self._sheet[b[0]][b[1:]]

    return a + b

