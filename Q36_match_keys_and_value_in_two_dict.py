# Q36.Write a Python program to match key values in two dictionaries.
# Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# Expected output: key1: 1 is present in both x and y

dict1={'key1': 1, 'key2': 3, 'key3': 2}
dict2={'key1': 1, 'key2': 2}
for keys1 in dict1:
    for keys2 in dict2:
        if keys1==keys2:
            if dict1[keys1]==dict2[keys2]:
                print(keys1,':',dict1[keys1],'is present in both dict1 an dict2')
