# from operator import le
list=[1,2,3,4]
# Sample output:
# {1: {2: {3: {4: {}}}}}
list=[1,2,3,4]
new_d=dict={}
for i in list:
    dict[i]={}
    dict=dict[i]
print(new_d)





# global i
# i=-1
# # k=0
# def dict(num_list):
#     # req_dict={}
#     global i
#     if i<(len(num_list)-2):
#         global dict1
#         dict1={}
#         i+=1
#         dict1[num_list[i]]=dict(num_list)
#     else:
#         dict1[num_list[i]]={}
#     return(dict1)
# num_list = [1, 2, 3, 4]
# print(dict(num_list))




# why here updation is happening at the place of adding new item? 


# def nested_dict(num_list):
#     i=0
#     while i<len(num_list):
#         dict={}
#         dict[num_list[i]]=nested_dict()
#         i+=1
# i=0
# while i<len(num_list):



# print(nested_dict(num_list))




# def nested_dict(num_list):
#     i=0
#     while i<len(num_list):
#         dict={}
#         dict[num_list[i]]=nested_dict()
#         i+=1

# print(nested_dict(num_list))