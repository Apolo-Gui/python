A = None
B = None
C = None
CALC1 = None
CALC2 = None
CALCS = None
D = None
DIFERENCA = None

def read_integer():
  try:
    # read for Python 2.x
    return int(raw_input())
  except NameError:
    # read for Python 3.x
    return int(input())


A = read_integer()
B = read_integer()
C = read_integer()
D = read_integer()
CALC1 = A * B
CALC2 = C * D
DIFERENCA = CALC1 - CALC2
print(str("DIFERENCA = ") + str(DIFERENCA))
