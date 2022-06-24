# Q45.
# Write a Python program to remove a specified dictionary from a given list.
# Original list of dictionary:
list1=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color':
'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# Remove id #FF0000 from the said list of dictionary:
# [{'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color':
# 'Olive'}]

sp_value=input('enter the key,the dict containing that key do you want to remove from list:\n')
i=0
while i<len(list1):
    for keys in list1[i]:
        if list1[i][keys]==sp_value:
            # list1.pop(list1[i])
            list1.pop(i)
    i+=1
print(list1)

what's the problem here ?
