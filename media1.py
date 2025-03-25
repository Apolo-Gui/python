A = None
B = None
MEDIA = None
PESO1 = None
PESO2 = None
TOTAL = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


A = read_numeric()
B = read_numeric()
PESO1 = A * 3.5
PESO2 = B * 7.5
MEDIA = PESO1 + PESO2
TOTAL = "{:0.5f}".format((MEDIA / 11))
print(str("MEDIA = ") + str(TOTAL))
