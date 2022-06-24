# me left
student_data = {
    'id1':
        {
        'name': ['Sara'],
        'class': ['V'],
'subject_integration': ['english, math, science']
    },
'id2':
{'name': ['David'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id3':
{'name': ['Sara'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
'id4':{'name': ['Surya'],
'class': ['V'],
'subject_integration': ['english, math, science']
},
}

# req_dict={}
# for id in student_data:
#     for data in id:
#         if student_data[id][data][0] not in req_dict[id][data][0]:
#             req_dict[id][data][0]=student_data[id][data][0]
# print(req_dict)

result={}
for i,j in student_data.items():
    if j not in result.values():
        result[i]=j
        
print(result)
