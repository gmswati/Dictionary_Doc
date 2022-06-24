d1={'a':100,'b':200,'c':300}
d2={'a':300,'b':200,'d':400}
dict={}
for key in d1:
    if key in d2:
        dict[key]=d1[key]+d2[key]
    else:
        dict[key]=d1[key]
for key in d2:
    if key not in d1:
        dict[key]=d2[key]
print(dict)