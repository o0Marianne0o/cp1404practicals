numbers = [3, 1, 4, 1, 5, 9, 2]

# numbers[0] is 3
# numbers[-1] is 2
# numbers[3] is 1
# numbers[:-1] is [3, 1, 4, 1, 5, 9]
# numbers[3:4] is [1]
# 5 in numbers is True
# 7 in numbers is False
# "3" in numbers is False
# numbers + [6, 5, 3] is [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

print(numbers[0])
print(numbers[-1])
print(numbers[3])
print(numbers[:-1])
print(numbers[3:4])
print(5 in numbers)
print(7 in numbers)
print("3" in numbers)
print(numbers + [6, 5, 3])
numbers[0] = "ten"
print(numbers)
numbers[6] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)
