# 3.13.6: Functions & Variables, Part 3
# Ty Ter Avest
# 2.18.19

'''
def print_numbers(x):
    print(x)

print_number(13)
print_number(23)

# 4.14.4: Name & age
# Ty Ter Avest
# 2.18.19

def name_and_age(name, age):
    print('\n', 'Hi, my name is', name, 'and I am', age, 'years old!')

name_and_age('Mike', 33)
name_and_age('Zane', 18)
'''

# 4.14.5: Default Parameter Values
# Ty Ter Avest
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number: ', x)
    print('Second Number: ' + str(y))

print_two_numbers(34, 45)
print_two_numbers(78)