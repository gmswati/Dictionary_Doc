# Q50.Write a Python program to convert a given dictionary into a list of lists.
# Original Dictionary:
dict={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# Convert the said dictionary into a list of lists:
# [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
# Original Dictionary:
# {'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
# Convert the said dictionary into a list of lists:
# [['1', 'Austin Little'], ['2', 'Natasha Howard'], ['3', 'Alfred Mullins'], ['4', 'Jamie Rowe']]

# code of this Q:
req_list=[]
for keys in dict:
    my_dict=[]
    my_dict.append(keys)
    my_dict.append(dict[keys])
    req_list.append(my_dict)
print(req_list)