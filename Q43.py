# Q43.Write a Python program to create a dictionary grouping a sequence of key-value pairs
# into a dictionary of lists.
# Original list:
list1=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# Grouping a sequence of key-value pairs into a dictionary of lists:
# {'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}
i=0
my_list=[]
while i<len(list1):
    if list1[i][0] not in my_list:
        my_list.append(list1[i][0])
    i+=1
print(my_list)
i=0
my_dict={}
while i<len(my_list):
    j=0
    list=[]
    while j<len(list1):
        if list1[j][0]==my_list[i]:
            list.append(list1[j][1])
        j+=1
    my_dict[my_list[i]]=list
    i+=1
print(my_dict)


# how it is out of range?



    # for item in list1[i]:
