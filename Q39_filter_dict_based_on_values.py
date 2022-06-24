# Q39.Write a Python program to filter a dictionary based on values.
# Original Dictionary:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# Marks greater than 170:
# {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}
dict={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
my_dict={}
for keys in dict:
    if dict[keys]>170:
        my_dict[keys]=dict[keys]
print(my_dict)