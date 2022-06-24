# import re


n=int(input('enter the no. of keys you want to create:'))
st_pt=int(input('enter the starting pt. for your list_item in value of dict:'))
end_pt=int(input('enter the ending pt. for your list_item in value of dict:'))
# following code is for creating keys for dict.
i=0
keys=[]
while i<n:
    key=input('enter the key you want in dict:')
    keys.append(key)
    i+=1
# following code is for creating the dict:
req_dict={}
i=0
# l=0
j=st_pt-1
while i<n:
    while j<end_pt:
        list1=[]
        k=j+1
        while k<j+9:
            list1.append(k)
            k+=1
        print(list1)
        # for key in keys:
            # req_dict[key]=list1

        j+=9
        req_dict[keys[i]]=list1
    i+=1
print(req_dict)

# how to improve this code?
here also item of req_dict is upating at the place of adding..,why?
