"""
12. Read the buying price (cost), desired profit % and sales tax % 
    of a product and calculate the final sales price.
    Apply the sales tax on top of the buying price + profit
"""

buying_price = float(input("Buying price: "))
profit_percentage = float(input("Profit %: "))
sales_tax_percentage = float(input("Sales Tax %: "))

profit = buying_price * (profit_percentage / 100)
price_before_tax = buying_price + profit
sales_tax = price_before_tax * (sales_tax_percentage / 100)
sales_price = price_before_tax + sales_tax

print(f"Profit = {profit}")
print(f"Price before tax = {price_before_tax}")
print(f"Sales Tax = {sales_tax}")
print(f"Sales price = {sales_price}")