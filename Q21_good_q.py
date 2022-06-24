list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
i=0
R_set=set()
while i<len(list):
    for key in list[i]:
        R_set.add(list[i][key])
    # R_set.add(list[i])
    i+=1
print(R_set)




# a=set()
# list=['swati','pragati','nil','manu','swati']
# for i in range(5):
#     a.add(list[i])
# print(a)