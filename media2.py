TOTAL = None
MEDIA2 = None
PESO3 = None
MEDIA = None
PESO2 = None
PESO1 = None
C = None
B = None
A = None

def read_numeric():
  try:
    # read for Python 2.x
    return float(raw_input())
  except NameError:
    # read for Python 3.x
    return float(input())


A = read_numeric()
B = read_numeric()
C = read_numeric()
PESO1 = A * 2
PESO2 = B * 3
PESO3 = C * 5
MEDIA = PESO1 + PESO2
MEDIA2 = MEDIA + PESO3
TOTAL = "{:0.1f}".format((MEDIA2 / 10))
print(str("MEDIA = ") + str(TOTAL))
