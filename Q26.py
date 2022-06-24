my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
# Sample Output:
# C1 C2 C3
# 1 5 9
# 2 6 10
# 3 7 11

for keys in my_dict:
    print(keys,end=' ')
i=0
print()
while i<len(my_dict[keys]):
    for keys in my_dict:
        # i=0
        # while i<len(my_dict[keys]):
        print(my_dict[keys][i],end=' ')
    print()
    i+=1