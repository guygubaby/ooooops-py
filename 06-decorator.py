
def time_used(func):
  def wrap_func(*args,**kw):
    print('start')
    func()
    print('end')
  return wrap_func


@time_used
def test():
  print('hh')

if __name__ == "__main__":
  test()