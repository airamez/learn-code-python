"""
11. Read the buying price (cost), and desired profit percentage and calculate the 
    sales price of the product.
"""

buy_price = float(input("Buy Price: "))
desired_profit_percentage = float(input("Desired profit %: "))

profit = buy_price * desired_profit_percentage / 100
sales_price = buy_price + profit

print(f"Sale price = {round(sales_price, 2)}; Profit: {round(profit, 2)}")