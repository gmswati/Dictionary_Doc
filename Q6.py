dict={0:10,1:20}
len=int(input('enter the no. of element you want to add in your dict:\n'))
i=1
while i<=len:
    key=input('enter the key you want:\n')
    Value=input('enter the value you want to add in dict:\n')
    dict[key]=Value
    i+=1
print(dict)

