# Q44.Write a Python program to split a given dictionary of lists into list of dictionaries.
# Original dictionary of lists:
dict= {'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# Split said dictionary of lists into list of dictionaries:[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language':
# 84}, {'Science': 95, 'Language': 80}]
my_list=[]

i=0
while i<4:
    dict1={}
    for key in dict:
        dict1[key]=dict[key][i]
    my_list.append(dict1)
    i+=1
# print(my_list)


# if output: [{'science':88},{'science':89},{'science':62},{'science':95},{'Language':77},{'Language':78},{'Language':84},{'Language':80}]

my_list=[]
for key in dict:
    i=0
    while i<len(dict[key]):
        my_dict={}
        my_dict[key]=dict[key][i]
        my_list.append(my_dict)
        i+=1

print(my_list)

