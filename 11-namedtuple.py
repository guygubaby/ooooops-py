from collections import namedtuple

Dog = namedtuple('Dog','name age sex')

d1 = Dog('guygubaby',23,'man')


print(d1.age)