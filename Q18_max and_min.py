dict_1={'anand':99,'amisha':70,'shruti':89,'deepak':80,'kaushal':50, "z":30}
# highest=max(dict,key=dict.get)
# smallest=min(dict,key=dict.get)
# print(highest)
# print(smallest)

# try to understand ^ its working

a=dict(sorted(dict_1.items(),key=lambda x:x[1]))
# print(a)
l=len(a)
c=0
for item in dict_1:
    c+=1
    if c==1:
        print('min_value is',item,'=',dict_1[item])
    if c==len(a):
        print('max_value is',item,'=',dict_1[item])
    

