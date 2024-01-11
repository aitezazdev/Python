book = float(input("Enter the price of the book : "))

no_Books = float(input("How many books you want to order : "))

total_Books_Prices = book * no_Books

tax = total_Books_Prices * (7.5 / 100)

shipping_Price = 20

total_price = total_Books_Prices + tax + shipping_Price
# Round the total price to 2 decimal places
total_price = round(total_price, 2)

print("Total price is ", total_price,"$")