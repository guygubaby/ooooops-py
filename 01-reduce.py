from functools import reduce


find_max = lambda a,b : a if a>=b else b


if __name__ == "__main__":
    lst = [32,2,12,31,23,1,23,123]
    res = reduce(find_max,lst)
    print(res)