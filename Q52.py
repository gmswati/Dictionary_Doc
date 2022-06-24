# Q52. Write a Python program to find the specified number of maximum values in a given
# dictionary.
# Original Dictionary:
dict={'a': 5, 'b': 14, 'c': 32, 'd': 35, 'e': 24, 'f': 100, 'g': 57, 'h': 8, 'i': 100}
# 1 maximum value(s) in the said dictionary:
# ['f']
# 2 maximum value(s) in the said dictionary:['f', 'i']
# 5 maximum value(s) in the said dictionary:
# ['f', 'i', 'g', 'd', 'c']

# code of this ques:-
n=int(input('enter the no. of highest values do you want:'))

for keys in dict:
    for item in dict:
        if dict[keys]<dict[item]:
            b=dict[keys]
            dict[keys]=dict[item]
            dict[item]=b

            a=keys
            keys=item
            item=a
print(dict)

c=0
list=[]
for keys in dict:
    c+=1
    if c<=5:
        list.append(keys)
    else:
        break
print(n,'maximum value(s) in the said dictionary:')
print(list)

HOw to improve it?

# for keys in dict:
#     for item in dict:
#         if dict[keys]<dict[item]:
#             a=keys
#             keys=item
#             item=a

#             b=dict[keys]
#             dict[keys]=dict[item]
#             dict[item]=b
# print(dict)

