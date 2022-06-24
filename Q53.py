# Q53.
# Write a Python program to convert a given list of lists to a dictionary.
# Original list of lists:
list=[[1, 'Jean Castro', 'V'], [2, 'Lula Powell', 'V'], [3, 'Brian Howell', 'VI'], [4, 'Lynne Foster', 'VI'], [5,
'Zachary Simon', 'VII']]
# Convert the said list of lists to a dictionary:
# O.P:-{1: ['Jean Castro', 'V'], 2: ['Lula Powell', 'V'], 3: ['Brian Howell', 'VI'], 4: ['Lynne Foster', 'VI'], 5:
# ['Zachary Simon', 'VII']}

i=0
dict={}
while i<len(list):
    my_list=[]
    j=1
    while j<len(list[i]):
        my_list.append(list[i][j])
        j+=1
    dict[list[i][0]]=my_list
    i+=1
print(dict)
