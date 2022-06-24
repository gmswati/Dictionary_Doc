# Q33.Python: Print a dictionary line by line
students = {'Aex':{'class':'V','rolld_id':2},
            'Puja':{'class':'V','roll_id':3}}
# Sample Output:
# Aex
# class : V
# rolld_id : 2Puja
# class : V
# roll_id : 3
for student in students:
    print(student)
    for k,v in students[student].items():
        print(k,':',v)
        