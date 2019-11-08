lst = [123,2,3,123,1,23]

print(sorted(lst))

additional_lst = [4,5]

lst.append(additional_lst)
print(lst)
lst.extend(additional_lst)
print(lst)