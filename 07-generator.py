
def genfibon(n:int):
  a = 1
  b = 1

  for i in range(n):
    yield a
    a,b = b,a+b


if __name__ == "__main__":
    g = genfibon(10)

    print(next(g))