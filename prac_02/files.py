# program 1 - Enter a name and save to text file
username = input("Enter your name: ")
output_file = open("name.txt", 'w')

print("{}".format(username), file=output_file)
output_file.close()

# program 2 - open file and print the stored name
open_file = open("name.txt", 'r')
print("Your name is {}".format(open_file.read()))
open_file.close()

# program 3 - adding stored value in the text file
number_file = open("numbers.txt", 'r')
first_number = int(number_file.readline())
second_number = int(number_file.readline())
sum_of_two_numbers = first_number + second_number
print("the sum of the two number is {}".format(sum_of_two_numbers))

# program 4 - sum of all numbers in numbers.txt
all_numbers = (number_file.readlines())
sum_of_numbers = 0

for numbers in all_numbers:
    all_number = int(numbers)
    sum_of_numbers += all_number
number_file.close()
print("The sum of all numbers is {}".format(sum_of_numbers))
