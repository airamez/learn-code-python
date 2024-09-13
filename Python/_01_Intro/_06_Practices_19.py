"""
19. Read the description, quantity and unit price of 3
    products in a shopping cart and print the total
    sales tax and the total order amount.
    The sales tax is 12%
"""

descritpion_1 = input("Product 1 Description: ")
quantity_1 = int(input("Product 1 Quantity: "))
price_1 = float(input("Product 1 Price: "))

descritpion_2 = input("Product 2 Description: ")
quantity_2 = int(input("Product 2 Quantity: "))
price_2 = float(input("Product 2 Price: "))

descritpion_3 = input("Product 3 Description: ")
quantity_3 = int(input("Product 3 Quantity: "))
price_3 = float(input("Product 3 Price: "))

total_before_tax = (quantity_1 * price_1) + \
                   (quantity_2 * price_2) + \
                   (quantity_3 * price_3)

sales_tax = (12 / 100) * total_before_tax

total_amount = total_before_tax + sales_tax

print(f"Sales tax: {sales_tax}")
print(f"Total order amount: {total_amount}")