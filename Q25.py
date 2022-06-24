str='w3resource'
dict={}
i=0
c=1
while i<len(str):
    if str[i] not in dict:
        dict[str[i]]=1
    else:
        c+=1
        dict[str[i]]=c
    i+=1
print(dict)