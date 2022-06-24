word='w3resource'
dict={}
for letter in word:
    if letter not in dict:
        dict[letter]=1
    else:
        # lette=dict[letter]+1
        # dict[letter]=lette
        dict[letter]+=1
print(dict)

# following is the concept that, how dict[letter]+=1 is working?
# dict[letter]=dict[letter]+1
# the 1st dict[letter] which is before equal sign is used for updation i.e, update the specified key.
# dict['e']=2+1