dict_1={'1':['a','b'],'2':['c','d']}
list_v=list(dict_1.values())
print(list_v)
for i in list_v[0]:
    for j in list_v[1]:
        s=i+j
        print(s)


# Method-2

# a={"1":["a","b"],"2":["c","d"]}
# for i in a["1"]:
#     for j in a["2"]:
#         print(i+j)
