class DoSth:
  def __init__(self,n:int):
    print('do ...')
    self.n = n

  def __enter__(self):
    print('enter')
    # raise ValueError('test error')
    return self.n + 1

  def __exit__(self,exc_type,exc_value,exc_trackback):
    print('exit')
    if exc_trackback is not None:
      print('error ',exc_value,exc_type,exc_trackback)


if __name__ == "__main__":
    with DoSth(3) as d:
      print(d)