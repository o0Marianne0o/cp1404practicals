total_price = 0
discounted_price = 0
number_of_items = int(input("Number of items: "))

while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Number of items: "))

for price in range(number_of_items):
    price_of_item = (float(input("Enter the price: ")))
    total_price += price_of_item

if total_price > 100:
    total_price *= 0.9
    print("Total price with for {} items is ${:.2f}(10% Discount applied)".format(number_of_items, total_price))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items, total_price))
