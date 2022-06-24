dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dict={}
for key in dic1:
    dict[key]=dic1[key]
for key in dic2:
    dict[key]=dic2[key]
for key in dic3:
    dict[key]=dic3[key]
print(dict)

# trying to make code universal:
# for key in dic1:
#     if key in (dic2 or dic3):
#         dict[key]=dic1[key]+dic2[key]+dic3[key]
#     else:
#         dict[key]=dic1[key]
#         dict[key]=dic2[key]
#         dict[key]=dic3[key]
# for key in dic2:
#     if key in dic3:
#         dict[key]=dic1[key]+dic2[key]+dic3[key]
#     else:
#         # dict[key]=dic1[key]
#         dict[key]=dic2[key]
#         dict[key]=dic3[key]
# for key in dic3:
#     if key in (dic2 or dic3):
#         dict[key]=dic1[key]+dic2[key]+dic3[key]
#     else:
#         # dict[key]=dic1[key]
#         # dict[key]=dic2[key]
#         dict[key]=dic3[key]
# print(dict)


