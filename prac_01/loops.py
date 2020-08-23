"""a"""
for i in range(0, 110, 10):
    print(i, end=' ')
print()
"""b"""
for i in range(20, 0, -1):
    print(i, end=' ')
print()
"""c"""
number_of_stars = int(input("Number of stars: "))
for star in range(1):
    number_of_stars = "*" * number_of_stars
    print(number_of_stars)
"""d"""
number_of_stars = int(input("Number of stars: "))
for star in range(number_of_stars + 1):
    number_of_stars = "*" * star
    print(number_of_stars)
