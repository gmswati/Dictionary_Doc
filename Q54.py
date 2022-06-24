# Q54.
# Write a Python program to create a key-value list pairings in a given dictionary.
# Original dictionary:
dict={1: ['Jean Castro'], 2: ['Lula Powell'], 3: ['Brian Howell'], 4: ['Lynne Foster'], 5: ['Zachary Simon']}
# A key-value list pairings of the said dictionary:
# [{1: 'Jean Castro', 2: 'Lula Powell', 3: 'Brian Howell', 4: 'Lynne Foster', 5: 'Zachary Simon'}]

# code of this Q.:-

req_list=[]
my_dict={}
for keys in dict:
    my_dict[keys]=dict[keys][0]
req_list.append(my_dict)
print(req_list)

