"""
# read the id, description, price and quantity of a product
  and print the content using the format below:
  {id: [ID], description: [DESCRIPTION], price: [PRICE], quantity: [QUANTITY], total: [PRICE * QUANTITY]}
  Example:
  INPUT
    ID: 123
    Description: Python Programming Book
    Price: 34.75
    Quantity: 3
  OUTPUT
    {id: [123], description: [Python Programming Book], price: [34.75], quantity: 3, total: 104.25}
"""

id = input("ID: ")
description = input("Description: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

output = f"{{id: [{id}], description: [{description}], price: [{price}], quantity: {quantity}, total: {total}}}"

print(output)