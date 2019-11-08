def test(*args,**kw):
  print(args)
  print(kw)


if __name__ == "__main__":
    test(1,23,4,name='yjb')

    lst = [1,3,2,34,234]
    test(*lst)