dict={'name1':'swati','name2':'pragati','name3':'mahalaxmi','name4':'partima'}
for keys in dict:
    for item in dict:
        if dict[keys]<dict[item]:
            b=keys
            keys=item
            item=b
            a=dict[keys]

            c=dict[keys]
            dict[keys]=dict[item]
            dict[item]=c
print(dict)

# print()

# it's done. :)

# here is also updating at the place of adding? why?


dict={'name1':'swati','name2':'pragati','name3':'mahalaxmi','name4':'partima'}
for keys in dict:
    for item in dict:
        if dict[keys]<dict[item]:

            c=dict[keys]
            dict[keys]=dict[item]
            dict[item]=c

            b=keys
            keys=item
            item=b
            a=dict[keys]
print(dict)

# how to improve this coding?

# but both are giving same output..., how?


dict={'name1':'swati','name2':'pragati','name3':'mahalaxmi','name4':'partima'}
for keys in dict:
    for item in dict:
        if dict[keys]<dict[item]:

            b=keys
            c=dict[keys]
            keys=item
            dict[keys]=dict[item]
            item=b
            dict[item]=c

            a=dict[keys]
print(dict)
