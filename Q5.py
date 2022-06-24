dict_1={1:2,3:4,4:3,2:1,0:0}
# a_dict=[]
# a=dict.sort()
# a_dict.append(a,key=dict.get)
# print(a_dict)

# sorted by values:
print(sorted(dict_1.values()))


#dictionary in assending order by value:
            # or
# sorted by values in the form of tuple:
print(sorted(dict_1.items(),key=lambda x:x[1]))

# Dictionary in desending order by value:
print(dict(sorted(dict_1.items(),key=lambda x:x[1],reverse=True)))
