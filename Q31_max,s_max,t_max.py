# Q31.. Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55,'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# # item3 41.3

# dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=dict['item1']
# # s_max=dict['item1']
# s_max=min(dict.values())
# # t_max=dict['item1']
# t_max=min(dict.values())
# # print(t_max,"8")
# for keys in dict:
#     if max<dict[keys]:
#         max=dict[keys]
#     if s_max<dict[keys] and dict[keys]!=max:
#         s_max=dict[keys]
#     if t_max<dict[keys] and dict[keys]!=max and dict[keys]!=s_max:
#         t_max=dict[keys]
# # print(dict)
# print(max)
# print(s_max)
# print(t_max)

# # t_max is not working why?





# # for keys1 in dict:
# #     for keys2 in dict:
# #         if dict[keys1]<dict[keys2]:


# # foll0wing code is correct :)
#      ^^^^^^^^^^^       #

# dict={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# max=dict['item1']
# # s_max=dict['item1']
# s_max=min(dict.values())
# # t_max=dict['item1']
# t_max=min(dict.values())
# # print(t_max,"8")
# for keys in dict:
#     if max<dict[keys]:
#         max=dict[keys]
# for keys in dict:
#     if s_max<dict[keys] and dict[keys]!=max:
#         s_max=dict[keys]
# for keys in dict:
#     if t_max<dict[keys] and dict[keys]!=max and dict[keys]!=s_max:
#         t_max=dict[keys]
# # print(dict)
# print(max)
# print(s_max)
# print(t_max)

# # finally I did It:)
