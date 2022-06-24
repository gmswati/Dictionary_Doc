# Q41.Write a Python program to filter the height and weight of students, which are stored in a
# dictionary.
# Original Dictionary:
dict={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# O.P:-
# Height > 6ft and Weight> 70kg:
# {'Cierra Vega': (6.2, 70)}

my_dict={}
for keys in dict:
    if dict[keys][0]>6 and dict[keys][1]:
        my_dict[keys]=dict[keys]
print(my_dict)