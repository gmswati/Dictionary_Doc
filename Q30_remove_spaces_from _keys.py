# Q30.Write a Python program to remove spaces from dictionary keys.
Org_dict={'S  001': ['Math', 'Science'], 'S   002': ['Math','English']}
# New dictionary: {'S001': ['Math', 'Science'], 'S002': ['Math','English']}
my_dict={}
for keys in Org_dict:
    i=0
    k=''
    while i<len(keys):
        if keys[i]==' ':
            pass
        else:
            k+=keys[i]
        i+=1
    my_dict[k]=Org_dict[keys]
print(my_dict)