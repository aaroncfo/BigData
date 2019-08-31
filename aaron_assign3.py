# Question D
num_list = [10, 20, 30, 40, 50]
print('The length of the list is', len(num_list), '\n')

for num in num_list:
    print(num, end=',')
print('\n')

for num in num_list:
    print('The square of', num, 'is', num**2)

num_list.append(60)
print('\n', 'The number 60 has been added to the list as shown below:\n', num_list)

num_list.remove(20)
print('\n', 'The number 20 has been removed from the list as shown below:\n', num_list)


#Question E
emp = [['John', 4500], ['Paul', 5000], ['Mary', 6000], ['Dave', 5500]]

dict_sal = {}
key_idx = 0
val_idx = 1


# Loop through list of lists and append to the dictionary
for item in emp:
    key = item[key_idx]
    val = item[val_idx]
    dict_sal[key] = val


for k, v in dict_sal.items():
    print(k, v)


text = '\'s salary is'
for k, v in dict_sal.items():
    print(k + text, v)


dict_sal['Judith'] = 5600
