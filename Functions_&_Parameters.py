# 3.13.6: Functions & Variables, Part 3
# Ty Ter Avest
# 2.18.19


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

print('Git Commit')
# 4.14.5: Default Parameter Values
# Ty Ter Avest
# 2.19.19

def print_two_numbers(x, y = 20):
    print('First number: ', x)
    print('Second Number: ' + str(y))

print_two_numbers(34, 45)
print_two_numbers(78)


# 4.14.6: Print Sum
# Ty Ter Avest
# 2.19.19

def print_sum(x, y):
    print(x + y)

print_sum(79,179)

# 4.14.7: Print Multiple Times
# Ty Ter Avest
# 2.19.19

def print_multiple_times(string, times):
    for i in range(times):
        print(string)

print_multiple_times('Hey there Computer Scientist',7)







