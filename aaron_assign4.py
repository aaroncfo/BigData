#Question H
num_a = 10
num_b = 7
if num_a < num_b:
    print(num_b, 'is the highest number', '\n',
          num_a, 'is the smallest number')

elif num_a == num_b:
    print('The numbers are equal')
else:
    print(num_a, 'is the highest number', '\n',
          num_b, 'is the smallest number')


h_val = 10
l_val = -1
while h_val > l_val:
    print(h_val)
    h_val += l_val


my_first_name = 'Aaron'
name_len = len(my_first_name)
for i in range(0, name_len):
    print(my_first_name[i])


fruits = ['orange', 'apple', 'mango', 'pineapple', 'pear']
for item in fruits:
    print(item)
