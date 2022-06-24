# Q40. Write a Python program to convert more than one list to nested dictionary.
# Original strings:
list1=['S001', 'S002', 'S003', 'S004']
list2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
list3=[85, 98, 89, 92]
# O.P:-
# Nested dictionary:
# [{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, {'S003': {'Duncan Boyle': 89}},
# {'S004': {'Saim Richards': 92}}]
i=0
req_list=[]
while i<len(list1):
    dict1={}
    dict2={}
    # dict2[list2[i]]=list3[i]
    # dict1[list1[i]]=dict2
    # dict2.update({list2[i]:list3[i]})
    # dict1.update({list1[i]:dict2})
    i+=1
req_list.append(dict1)
print(req_list)

why here items are updating not adding/appening?
how to append items then?
