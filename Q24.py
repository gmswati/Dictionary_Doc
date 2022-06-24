list=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1',
'amount': 750}]
i=0
my_list=[]
while i<len(list):
    # list_values=list[i]['item'])
    if list[i]['item'] not in my_list:
        my_list.append(list[i]['item'])
    i+=1
# print(list_values)
print(my_list)
i=0
dict1={}
while i<len(my_list):
    j=0
    sum=0
    # req_list=[]
    while j<len(list):
        if my_list[i]==list[j]['item']:
           sum+=list[j]['amount']
        j+=1
    dict1[my_list[i]]=sum
    # req_list['item']=my_list[i]
    # req_list['amount']=sum
    i+=1
# print(req_list)
print(dict1)
        



# i=0
# my_list=[]
# while i<len(list):
#     # for key in list[i]:
#     if list[i]['item']==
