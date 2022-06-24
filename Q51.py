# Q51.Write a Python program to filter even numbers from a given dictionary values.
# Original Dictionary:
dict={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# Filter even numbers from said dictionary values:
# {'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}
# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# Filter even numbers from said dictionary values:
# {'V': [], 'VI': [], 'VII': [2]}

# code of this Q:

# for keys in dict:
#     i=0
#     while i<len(dict[keys]):
#         if dict[keys][i]%2!=0:
#             dict.pop(dict[keys][i])
#         i+=1
# print(dict)

# what's problem in upper code?


req_dict={}
for keys in dict:
    i=0
    list=[]
    while i<len(dict[keys]):
        if dict[keys][i]%2==0:
            list.append(dict[keys][i])
        i+=1
    req_dict[keys]=list
print(req_dict)





