# 1 - Basic list operations
numbers = []
for item in range(0, 5):
    number = int(input("Number: "))
    numbers.append(number)

print("The first number is {}".format(numbers[0]))
print("The last number is {}".format(numbers[-1]))
print("the smallest number is {}".format(min(numbers)))
print("the largest number is {}".format(max(numbers)))
print("the average of the numbers is {}".format(sum(numbers)/len(numbers)))

# 2 - Woefully inadequate security checker
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
user_input = False
while user_input is not True:
    if username in usernames:
        print("Access granted!")
        user_input = True
    else:
        print("Access denied!")
        username = input("Enter username: ")
