# #code to create dictionary:
# len=int(input('enter the no. of element do you want in your dict:\n'))
# i=1
# dict={}
# while i<=len:
#     key=input('enter the key name:\n')
#     value=input('enter the value:\n')
#     dict[key]=value
#     i+=1
# print(dict)
dict={1:500,2:100,5:1000,3:200}
for key in dict:
    print(key)
    print(dict[key])
