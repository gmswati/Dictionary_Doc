# Q38.. Write a Python program to drop empty Items from a given Dictionary.
# Original Dictionary:
dict={'c1': 'Red', 'c2': 'Green', 'c3': None}
# New Dictionary after dropping empty items:
#{'c1'}:'Red','c2':'Green'}

for keys in dict:
    if dict[keys]==None or dict[keys]=='' or dict[keys]==0:
        # dict.popitem(dict[keys])
        # dict.pop()
        dict.pop(keys)

        # del dict[keys]

print(dict)

how to improve this code?
