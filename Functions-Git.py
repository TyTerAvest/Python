# Ty Ter Avest
# 2.5.19 Python - Exceptions - Git

name = input("What is your name:")

def greeting():
    print("Hi there " + name + "!")
    print("Nice to meet you")

greeting()



# 4.13.4: Functions and Variables
# Ty Ter Avest
# 2.11.19

x = 406

def print_something():
    x = 3
    print ('\n', x)

print('\n', x)
print_something()


# 4.13.5: Functions and Variables, Part 2
# Ty Ter Avest

my_variable = 3.6745

def something():
    print (my_variable + 10)


something()


# 4.13.6: Functions and Variables, Part 3
# Ty Ter Avest

z = 12.345

def print_something():
    z = 'hi '
    print (z * 7)

print_something()


print (round(z * 3, 2))


# 4.16.3: Enter a Number using Try & Except
# Ty Ter AVest
# 2.20.19


try:
    my_num = int(input('Enter an interger: '))
    print('Your number:', my_num)

except ValueError:
    print('\n''That was not an integer, YOU FOOL!')